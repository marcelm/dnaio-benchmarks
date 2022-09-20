#!/usr/bin/env python3

import sys

from Bio import SeqIO

if __name__ == "__main__":
    record_iterator = SeqIO.parse(sys.argv[1], "fastq")
    with open(sys.argv[2], "wt") as out_file:
        SeqIO.write(record_iterator, out_file, "fastq")


