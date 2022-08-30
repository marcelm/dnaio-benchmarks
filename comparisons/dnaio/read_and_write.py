#!/usr/bin/env python3

import dnaio
import sys

if __name__ == "__main__":
    with dnaio.open(sys.argv[1], mode="r") as in_records:
        with open(sys.argv[2], mode="wb") as out_file:
            for record in in_records:  # dnaio.SequenceRecord
                out_file.write(record.fastq_bytes())
