#!/usr/bin/env python3

import pyfastx
import sys

if __name__ == "__main__":
    records = pyfastx.Fastq(sys.argv[1])
    for record in records:
        pass