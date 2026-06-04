#!/usr/bin/env python3
"""Small fixture tool used to validate a command schema."""

from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert CSV input into a report.")
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument("--output", required=True, help="Output report path")
    parser.add_argument("--format", required=True, choices=["json"], help="Output format")
    parser.parse_args()


if __name__ == "__main__":
    main()
