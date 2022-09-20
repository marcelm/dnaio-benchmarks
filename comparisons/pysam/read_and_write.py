import sys

from pysam import FastxFile

if __name__ == "__main__":
    # returns pysam.libcfaidx.FastxRecord instances
    with FastxFile(sys.argv[1]) as f:
        with open(sys.argv[2], mode='w') as fout:
            for record in f:
                fout.write(str(record) + "\n")
