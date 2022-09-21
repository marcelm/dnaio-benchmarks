#!/usr/bin/env python3

import pyfastx
import sys

if __name__ == "__main__":
    # Do not build index, to save SSD and because this is described as fastest.
    records = pyfastx.Fastq(sys.argv[1], build_index=False, full_name=True)
    for record in records:
        pass
