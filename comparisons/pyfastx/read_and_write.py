#!/usr/bin/env python3

import pyfastx
import sys

if __name__ == "__main__":
    in_records = pyfastx.Fastq(sys.argv[1])
    with open(sys.argv[2], mode="wt", encoding="ascii") as out_file:
        for record in in_records:  # dnaio.SequenceRecord
            out_file.write(record.raw)
