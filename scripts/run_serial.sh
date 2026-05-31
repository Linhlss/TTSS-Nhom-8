#!/usr/bin/env bash
set -euo pipefail
N="${1:-100000000}"
make serial
./bin/pi_serial "$N"
