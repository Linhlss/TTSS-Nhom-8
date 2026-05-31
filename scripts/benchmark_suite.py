#!/usr/bin/env python3
import csv
import os
import statistics
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT_DIR = ROOT / "results"
RESULT_DIR.mkdir(exist_ok=True)

MPIRUN = os.environ.get("MPIRUN", "/opt/homebrew/bin/mpirun")
SUMMARY_FIELDS = [
    "experiment", "mode", "N", "workers", "repeat", "pi", "error",
    "time_sec", "time_std", "speedup", "efficiency", "efficiency_percent",
    "notes",
]
RAW_FIELDS = [
    "experiment", "mode", "N", "workers", "trial", "pi", "error", "time_sec",
]


def run_program(command):
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    lines = [line.strip() for line in completed.stdout.splitlines() if line.strip()]
    if len(lines) < 2:
        raise RuntimeError(
            f"Unexpected output from {' '.join(command)}:\n"
            f"{completed.stdout}\n{completed.stderr}"
        )
    return dict(zip(lines[-2].split(","), lines[-1].split(",")))


def command_for(mode, n, workers):
    if mode == "serial":
        return ["./bin/pi_serial", str(n)]
    if mode == "openmp":
        return ["./bin/pi_openmp", str(n), str(workers)]
    if mode == "mpi":
        return [MPIRUN, "-np", str(workers), "./bin/pi_mpi", str(n)]
    raise ValueError(f"Unsupported mode: {mode}")


def measure(experiment, mode, n, workers, repeat, raw_rows, notes=""):
    rows = []
    for trial in range(1, repeat + 1):
        row = run_program(command_for(mode, n, workers))
        rows.append(row)
        raw_rows.append({
            "experiment": experiment,
            "mode": row["mode"],
            "N": row["N"],
            "workers": row["workers"],
            "trial": trial,
            "pi": row["pi"],
            "error": row["error"],
            "time_sec": row["time_sec"],
        })

    times = [float(row["time_sec"]) for row in rows]
    first = rows[0]
    return {
        "experiment": experiment,
        "mode": first["mode"],
        "N": first["N"],
        "workers": first["workers"],
        "repeat": repeat,
        "pi": first["pi"],
        "error": first["error"],
        "time_sec": f"{statistics.mean(times):.9f}",
        "time_std": f"{statistics.pstdev(times):.9f}" if repeat > 1 else "0.000000000",
        "speedup": "",
        "efficiency": "",
        "efficiency_percent": "",
        "notes": notes,
    }


def add_strong_metrics(row, serial_time):
    workers = int(row["workers"])
    elapsed = float(row["time_sec"])
    speedup = serial_time / elapsed if elapsed > 0 else 0.0
    efficiency = speedup / workers if workers > 0 else 0.0
    row.update({
        "speedup": f"{speedup:.6f}",
        "efficiency": f"{efficiency:.6f}",
        "efficiency_percent": f"{efficiency * 100:.2f}",
    })
    return row


def write_csv(path, fieldnames, rows):
    with path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def generate_tables(n_rows, strong_rows, weak_rows):
    strong_parallel = [row for row in strong_rows if row["mode"] != "serial"]
    workers = sorted({int(row["workers"]) for row in strong_parallel})
    strong_table = []
    for worker in workers:
        openmp = next(row for row in strong_parallel if row["mode"] == "openmp" and int(row["workers"]) == worker)
        mpi = next(row for row in strong_parallel if row["mode"] == "mpi" and int(row["workers"]) == worker)
        strong_table.append({
            "workers": worker,
            "openmp_time_sec": openmp["time_sec"],
            "mpi_time_sec": mpi["time_sec"],
            "openmp_speedup": openmp["speedup"],
            "mpi_speedup": mpi["speedup"],
            "openmp_efficiency_percent": openmp["efficiency_percent"],
            "mpi_efficiency_percent": mpi["efficiency_percent"],
        })
    write_csv(
        RESULT_DIR / "table_strong_scaling.csv",
        list(strong_table[0].keys()),
        strong_table,
    )

    n_values = sorted({int(row["N"]) for row in n_rows})
    error_table = []
    for n in n_values:
        by_mode = {row["mode"]: row for row in n_rows if int(row["N"]) == n}
        error_table.append({
            "N": n,
            "serial_error": by_mode["serial"]["error"],
            "openmp_error": by_mode["openmp"]["error"],
            "mpi_error": by_mode["mpi"]["error"],
        })
    write_csv(RESULT_DIR / "table_error_by_n.csv", list(error_table[0].keys()), error_table)

    weak_table = []
    for row in weak_rows:
        weak_table.append({
            "mode": row["mode"],
            "workers": row["workers"],
            "N": row["N"],
            "time_sec": row["time_sec"],
            "weak_efficiency_percent": row["efficiency_percent"],
        })
    write_csv(RESULT_DIR / "table_weak_scaling.csv", list(weak_table[0].keys()), weak_table)


def main():
    repeat = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    n_values = [1_000_000, 10_000_000, 100_000_000, 1_000_000_000]
    workers = [1, 2, 4, 8]
    fixed_worker = 4
    strong_n = 100_000_000
    weak_base_n = 10_000_000

    subprocess.run(["make", "all"], cwd=ROOT, check=True)

    raw_rows = []
    n_rows = []
    strong_rows = []
    weak_rows = []

    for n in n_values:
        serial = measure("n_size", "serial", n, 1, repeat, raw_rows, "baseline for the same N")
        serial_time = float(serial["time_sec"])
        serial.update({"speedup": "1.000000", "efficiency": "1.000000", "efficiency_percent": "100.00"})
        n_rows.append(serial)
        n_rows.append(add_strong_metrics(measure("n_size", "openmp", n, fixed_worker, repeat, raw_rows), serial_time))
        n_rows.append(add_strong_metrics(measure("n_size", "mpi", n, fixed_worker, repeat, raw_rows), serial_time))

    serial = measure("strong_scaling", "serial", strong_n, 1, repeat, raw_rows, "shared Serial baseline")
    serial_time = float(serial["time_sec"])
    serial.update({"speedup": "1.000000", "efficiency": "1.000000", "efficiency_percent": "100.00"})
    strong_rows.append(serial)
    for mode in ("openmp", "mpi"):
        for worker in workers:
            strong_rows.append(add_strong_metrics(measure("strong_scaling", mode, strong_n, worker, repeat, raw_rows), serial_time))

    for mode in ("openmp", "mpi"):
        mode_rows = []
        for worker in workers:
            n = weak_base_n * worker
            mode_rows.append(measure(
                "weak_scaling",
                mode,
                n,
                worker,
                repeat,
                raw_rows,
                "N = 10^7 * workers",
            ))
        baseline = float(mode_rows[0]["time_sec"])
        for row in mode_rows:
            elapsed = float(row["time_sec"])
            efficiency = baseline / elapsed if elapsed > 0 else 0.0
            row.update({
                "speedup": "",
                "efficiency": f"{efficiency:.6f}",
                "efficiency_percent": f"{efficiency * 100:.2f}",
            })
            weak_rows.append(row)

    write_csv(RESULT_DIR / "raw_runs.csv", RAW_FIELDS, raw_rows)
    write_csv(RESULT_DIR / "n_size_results.csv", SUMMARY_FIELDS, n_rows)
    write_csv(RESULT_DIR / "strong_scaling_results.csv", SUMMARY_FIELDS, strong_rows)
    write_csv(RESULT_DIR / "weak_scaling_results.csv", SUMMARY_FIELDS, weak_rows)
    write_csv(
        RESULT_DIR / "openmp_mpi_comparison.csv",
        SUMMARY_FIELDS,
        [row for row in strong_rows if row["mode"] != "serial"],
    )
    generate_tables(n_rows, strong_rows, weak_rows)

    print("Saved complete benchmark suite to results/")
    print(f"Raw observations: {len(raw_rows)}")
    print(f"Summary rows: N-size={len(n_rows)}, strong={len(strong_rows)}, weak={len(weak_rows)}")


if __name__ == "__main__":
    main()
