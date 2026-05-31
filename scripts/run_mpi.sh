#!/usr/bin/env bash
set -euo pipefail
N="${1:-100000000}"
PROCESSES="${2:-4}"
make mpi
/opt/homebrew/bin/mpirun -np "$PROCESSES" ./bin/pi_mpi "$N"
