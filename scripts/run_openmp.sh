#!/usr/bin/env bash
set -euo pipefail
N="${1:-100000000}"
THREADS="${2:-4}"
make openmp
./bin/pi_openmp "$N" "$THREADS"
