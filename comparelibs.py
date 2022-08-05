import os
import dnaio
import io
import timeit

PATH = "data/paired300bp_1.fastq"


# https://pythonhosted.org/ngs_plumbing/parsing.html
# pip install ngs_plumbing
import ngs_plumbing.parsing

def ngs_plumbing_parsing(path):
    "ngs_plumbing.parsing.open"
    for record in ngs_plumbing.parsing.open(path):
        pass


# http://scikit-bio.org/
# pip install scikit-bio 'scipy<1.9'
import skbio.io

def skbio_io_read(path):
    "skbio.io.read"
    for r in skbio.io.read(path, format="fastq", phred_offset=33):
        pass


# From https://github.com/lh3/readfq/blob/091bc699beee3013491268890cc3a7cbf995435b/readfq.py

def _readfq(fp): # this is a generator function
    last = None # this is a buffer keeping the last unprocessed line
    while True: # mimic closure; is it a bad idea?
        if not last: # the first record or a record following a fastq
            for l in fp: # search for the start of the next record
                if l[0] in '>@': # fasta/q header line
                    last = l[:-1] # save this line
                    break
        if not last: break
        name, seqs, last = last[1:].partition(" ")[0], [], None
        for l in fp: # read the sequence
            if l[0] in '@+>':
                last = l[:-1]
                break
            seqs.append(l[:-1])
        if not last or last[0] != '+': # this is a fasta record
            yield name, ''.join(seqs), None # yield a fasta record
            if not last: break
        else: # this is a fastq record
            seq, leng, seqs = ''.join(seqs), 0, []
            for l in fp: # read the quality
                seqs.append(l[:-1])
                leng += len(l) - 1
                if leng >= len(seq): # have read enough quality
                    last = None
                    yield name, seq, ''.join(seqs); # yield a fastq record
                    break
            if last: # reach EOF before reading enough quality
                yield name, seq, None # yield a fasta record instead
                break


def readfq(path):
    "readfq"
    with open(path) as f:
        for record in _readfq(f):
            pass


# copied from https://github.com/lh3/readfq/pull/10/, but
# fixed so that the '@' from the record header is removed

import itertools

def _readfq2(fp): # this is a generator function
    rstrip = str.rstrip
    for aread in itertools.zip_longest(*[fp]*4):
        yield (rstrip(aread[0][1:]),rstrip(aread[1]),rstrip(aread[3]))


def readfq2(path):
    "readfq2"
    with open(path) as f:
        for record in _readfq2(f):
            pass


# pip install Bio
from Bio import SeqIO

def biopython_seqrecord(path):
    "Biopython Seqio.parse"
    for record in SeqIO.parse(path, "fastq"):
        pass


# pip install Bio
from Bio.SeqIO.QualityIO import FastqGeneralIterator

def biopython_tuples(path):
    "Biopython FastqGeneralIterator"
    for a_tuple in FastqGeneralIterator(path):
        pass


# pip install dnaio
import dnaio

def dnaio_open(path):
    "dnaio.open"
    for record in dnaio.open(path):
        pass


# pip install fastq-and-furious
import fastqandfurious.fastqandfurious as fqf

def fastqandfurious(path):
    "fastqandfurious.readfastq_iter"
    with open(path, "rb") as f:
        for record in fqf.readfastq_iter(f, 200000):
            pass


# https://www.reneshbedre.com/blog/filereaders.html#fastq-reader
# pip install bioinfokit
# - returns tuples, first element is header with '@' still included
from bioinfokit.analys import fastq as bioinfokit_fastq


def bioinfokit(path):
    "bioinfokit.analys.fastq.fastq_reader"
    for record in bioinfokit_fastq.fastq_reader(file=path):
        pass


# pip install pysam
from pysam import FastxFile

def pysam_fastxfile(path):
    "pysam.FastxFile"
    # returns pysam.libcfaidx.FastxRecord instances
    with FastxFile(path) as f:
        for record in f:
            pass


def main():
    for func in (
        dnaio_open,
        pysam_fastxfile,
        bioinfokit,
        ngs_plumbing_parsing,
        # skbio_io_read,  # super slow
        readfq,
        readfq2,
        biopython_seqrecord,
        biopython_tuples,
        fastqandfurious,
    ):
        path = PATH
        print(func.__doc__, timeit.repeat("func(path)", number=1, repeat=1, globals=locals()))


if __name__ == "__main__":
    main()
