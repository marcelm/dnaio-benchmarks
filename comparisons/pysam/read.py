import sys

from pysam import FastxFile

if __name__ == "__main__":
    # returns pysam.libcfaidx.FastxRecord instances
    with FastxFile(sys.argv[1]) as f:
        for record in f:
            pass