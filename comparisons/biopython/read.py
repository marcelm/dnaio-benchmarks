#!/usr/bin/env python3

import sys

from Bio import SeqIO

if __name__ == "__main__":
    for record in SeqIO.parse(sys.argv[1], "fastq"):
        pass

