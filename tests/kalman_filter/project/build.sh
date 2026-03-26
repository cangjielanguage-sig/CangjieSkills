#!/bin/bash
# Build script for the Kalman filter project
# This script compiles the C library and then builds the Cangjie project.
#
# Prerequisites:
#   - clang (C compiler)
#   - Cangjie SDK (cjpm, cjc) on PATH
#
# Usage:
#   chmod +x build.sh
#   ./build.sh          # Build the project
#   ./build.sh test     # Build and run tests
#   ./build.sh run      # Build and run demo

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Building C library ==="
mkdir -p libs
clang -shared -fPIC -fstack-protector-all c_src/kalman_filter.c -o libs/libkalman_filter.so -lm
echo "C library built: libs/libkalman_filter.so"

export LD_LIBRARY_PATH="$SCRIPT_DIR/libs:$LD_LIBRARY_PATH"

echo "=== Building Cangjie project ==="
cjpm build
echo "Build complete."

if [ "$1" = "test" ]; then
    echo "=== Running tests ==="
    cjpm test
elif [ "$1" = "run" ]; then
    echo "=== Running demo ==="
    cjpm run
fi
