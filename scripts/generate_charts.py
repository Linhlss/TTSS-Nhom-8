#!/usr/bin/env python3
import csv
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/ttss-pi-matplotlib")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp/ttss-pi-cache")
os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULT_DIR = ROOT / "results"
FIGURE_DIR = ROOT / "report" / "figures"
FIGURE_DIR.mkdir(parents=True, exist_ok=True)

COLORS = {"serial": "#355C7D", "openmp": "#D95F59", "mpi": "#2A9D8F"}
LABELS = {"serial": "Serial", "openmp": "OpenMP", "mpi": "MPI"}


def read_csv(name):
    with (RESULT_DIR / name).open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


def finish(filename, title, xlabel, ylabel, log_x=False, log_y=False):
    plt.title(title, fontweight="bold")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if log_x:
        plt.xscale("log")
    if log_y:
        plt.yscale("log")
    plt.grid(True, alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / filename, dpi=180)
    plt.close()


def line_chart(rows, metric, filename, title, xlabel, ylabel):
    plt.figure(figsize=(7.2, 4.6))
    for mode in ("openmp", "mpi"):
        selected = [row for row in rows if row["mode"] == mode]
        selected.sort(key=lambda row: int(row["workers"]))
        plt.plot(
            [int(row["workers"]) for row in selected],
            [float(row[metric]) for row in selected],
            marker="o",
            linewidth=2.2,
            color=COLORS[mode],
            label=LABELS[mode],
        )
    finish(filename, title, xlabel, ylabel)


def main():
    strong = read_csv("strong_scaling_results.csv")
    n_size = read_csv("n_size_results.csv")
    weak = read_csv("weak_scaling_results.csv")

    line_chart(
        strong, "time_sec", "time_strong_scaling.png",
        "Strong scaling: thời gian theo số worker", "Số worker", "Thời gian (giây)",
    )
    line_chart(
        strong, "speedup", "speedup_strong_scaling.png",
        "Strong scaling: speedup theo số worker", "Số worker", "Speedup",
    )
    line_chart(
        strong, "efficiency_percent", "efficiency_strong_scaling.png",
        "Strong scaling: efficiency theo số worker", "Số worker", "Efficiency (%)",
    )

    plt.figure(figsize=(7.2, 4.6))
    for mode in ("serial", "openmp", "mpi"):
        selected = [row for row in n_size if row["mode"] == mode]
        selected.sort(key=lambda row: int(row["N"]))
        plt.plot(
            [int(row["N"]) for row in selected],
            [float(row["error"]) for row in selected],
            marker="o",
            linewidth=2.2,
            color=COLORS[mode],
            label=LABELS[mode],
        )
    finish(
        "error_by_n.png",
        "Sai số tuyệt đối theo kích thước bài toán",
        "Số khoảng chia N",
        "Sai số tuyệt đối",
        log_x=True,
        log_y=True,
    )

    line_chart(
        weak, "time_sec", "time_weak_scaling.png",
        "Weak scaling: thời gian khi N tăng theo số worker",
        "Số worker", "Thời gian (giây)",
    )

    print(f"Saved charts to: {FIGURE_DIR}")


if __name__ == "__main__":
    main()
