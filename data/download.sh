#!/bin/bash
set -euo pipefail
set -x
# sra-tools 2.11.0

# - This uses --defline-qual '+' to avoid getting a second FASTQ header
# - The -F option gives original read names, but for some datasets this just results
#   reads named 1, 2, 3 etc., so we use --defline-seq '@$ac.$si' to get something
#   slightly longer (and therefore more realistic).

# 11387212 reads, 43 bp single-end
fastq-dump -F --defline-qual '+' SRR020285

# 2 x 150 bp paired-end, first 2 million reads
fastq-dump --split-3 --maxSpotId 2000000 --defline-seq '@$ac.$si' --defline-qual '+' SRR12131341

# 1380851 reads, 305 bp paired-end, MiSeq
fastq-dump --split-3 -F --defline-qual '+' ERR1760498

# 115769 reads, avg. length 9024 bp, PacBio
fastq-dump --defline-seq '@$ac.$si' --defline-qual '+' SRR2174302
