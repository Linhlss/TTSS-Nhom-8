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
        raise RuntimeError(f"Unexpected output from {' '.join(command)}:\n{completed.stdout}\n{completed.stderr}")

    header = lines[-2].split(",")
    values = lines[-1].split(",")
    return dict(zip(header, values))


def average_time(command, repeat):
    rows = []
    for _ in range(repeat):
        rows.append(run_program(command))
    times = [float(row["time_sec"]) for row in rows]
    first = rows[0]
    first["time_sec"] = f"{statistics.mean(times):.9f}"
    first["time_std"] = f"{statistics.pstdev(times):.9f}" if repeat > 1 else "0.000000000"
    return first


def parse_worker_list(text):
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def add_derived_metrics(row, baseline_time):
    worker_count = int(row["workers"])
    elapsed = float(row["time_sec"])
    speedup = baseline_time / elapsed if elapsed > 0 else 0.0
    efficiency = speedup / worker_count if worker_count > 0 else 0.0
    row.update({
        "speedup": f"{speedup:.6f}",
        "efficiency": f"{efficiency:.6f}",
        "efficiency_percent": f"{efficiency * 100:.2f}",
    })
    return row


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000_000
    repeat = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    threads_text = sys.argv[3] if len(sys.argv) > 3 else "1,2,4,8"
    processes_text = sys.argv[4] if len(sys.argv) > 4 else threads_text
    thread_values = parse_worker_list(threads_text)
    process_values = parse_worker_list(processes_text)

    subprocess.run(["make", "all"], cwd=ROOT, check=True)

    summary = []

    serial = average_time(["./bin/pi_serial", str(n)], repeat)
    serial_time = float(serial["time_sec"])
    serial.update({
        "speedup": "1.000000",
        "efficiency": "1.000000",
        "efficiency_percent": "100.00",
    })
    summary.append(serial)

    for threads in thread_values:
        row = average_time(["./bin/pi_openmp", str(n), str(threads)], repeat)
        summary.append(add_derived_metrics(row, serial_time))

    for processes in process_values:
        row = average_time([MPIRUN, "-np", str(processes), "./bin/pi_mpi", str(n)], repeat)
        summary.append(add_derived_metrics(row, serial_time))

    out_path = RESULT_DIR / "benchmark_result.csv"
    fieldnames = [
        "mode", "N", "workers", "pi", "error", "time_sec", "time_std",
        "speedup", "efficiency", "efficiency_percent",
    ]
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary)

    print(f"Saved benchmark result to: {out_path}")
    for row in summary:
        print(
            f"{row['mode']:>8} | workers={row['workers']:>2} | "
            f"time={row['time_sec']}s | speedup={row['speedup']} | "
            f"eff={row['efficiency_percent']}% | error={row['error']}"
        )


if __name__ == "__main__":
    main()
