#!/usr/bin/env python3

import dnaio
import sys

if __name__ == "__main__":
    with dnaio.open(sys.argv[1]) as records:
        for record in records:
            pass
