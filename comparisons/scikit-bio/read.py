#!/usr/bin/env python3

import sys
import skbio.io


if __name__ == "__main__":
    for r in skbio.io.read(sys.argv[1], format="fastq", phred_offset=33):
        pass
