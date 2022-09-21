#!/usr/bin/env python3

import functools
import xopen
import dnaio
import sys

# Open single threaded for a fair comparison with other tools.
OPENER = functools.partial(xopen.xopen, threads=0)

if __name__ == "__main__":
    with dnaio.open(sys.argv[1], mode="r", opener=OPENER) as in_records:
        with open(sys.argv[2], mode="wb") as out_file:
            for record in in_records:  # dnaio.SequenceRecord
                out_file.write(record.fastq_bytes())
