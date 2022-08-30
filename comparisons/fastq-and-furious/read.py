#!/usr/bin/env python3
import sys
import gzip

# This library doesn't do much for you when you simply want to open a fastq
# file. The newest dev version has an automagic open (to find whether a file
# is gzipped) but this is not released yet.
from fastqandfurious import fastqandfurious, _fastqandfurious

# Code mostly taken from their own benchmark code. The C-extension is the only
# interesting one to benchmark.
if __name__ == "__main__":
        filename = sys.argv[1]
        opener = gzip.open if filename.endswith(".gz") else open
        with opener(filename, "rb") as fastq_file:
            # Use same bufsize as dnaio
            fastq_iter = fastqandfurious.readfastq_iter(
                fastq_file, fbufsize=128 * 1024,
                _entrypos=_fastqandfurious.entrypos)
            for record in fastq_iter:
                pass

