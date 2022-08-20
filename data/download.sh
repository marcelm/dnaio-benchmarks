#!/bin/bash
set -euo pipefail
set -x
# sra-tools 2.11.0

# - This uses --defline-qual '+' to avoid getting a second FASTQ header
# - The -F option gives original read names, but for some datasets this just results
#   reads named 1, 2, 3 etc., so we use --defline-seq '@$ac.$si' to get something
#   slightly longer (and therefore more realistic).

# Fastq's gzipped with level 1. This is the most common gzip level for FASTQ files
# coming from sequencers.

# 43 bp single-end, 11387212 reads
fastq-dump -F --defline-qual '+' SRR020285
mv SRR020285.fastq single43bp.fastq
gzip -k -1 single43bp.fastq

# 2 x 150 bp paired-end, first 2 million reads
fastq-dump --split-3 --maxSpotId 2000000 --defline-seq '@$ac.$si' --defline-qual '+' SRR12131341
mv SRR12131341_1.fastq paired150bp_1.fastq
mv SRR12131341_2.fastq paired150bp_2.fastq
gzip -k -1 paired150bp_1.fastq
gzip -k -1 paired150bp_2.fastq

# 305 bp paired-end (MiSeq), 1380851 reads
fastq-dump --split-3 -F --defline-qual '+' ERR1760498
mv ERR1760498_1.fastq paired300bp_1.fastq
mv ERR1760498_2.fastq paired300bp_2.fastq
gzip -k -1 paired300bp_1.fastq
gzip -k -1 paired300bp_2.fastq

# avg. length 9024 bp (PacBio), 115769 reads
fastq-dump --defline-seq '@$ac.$si' --defline-qual '+' SRR2174302
mv SRR2174302.fastq single9000bp.fastq
gzip -k -1 single9000bp.fastq
