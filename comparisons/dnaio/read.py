#!/usr/bin/env python3

import dnaio
import xopen
import functools
import sys

# Open single threaded for a fair comparison with other tools.
OPENER = functools.partial(xopen.xopen, threads=0)

if __name__ == "__main__":
    with dnaio.open(sys.argv[1], opener=OPENER) as records:
        for record in records:
            pass
