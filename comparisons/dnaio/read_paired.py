#!/usr/bin/env python3

import dnaio
import sys

if __name__ == "__main__":
    with dnaio.open(sys.argv[1], file2=sys.argv[1], mode="r") as records:
        for record in records:
            pass
