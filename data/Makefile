# Run this with sra-tools 2.11.0

# Explanation for fastq-dump options:
#
# - We use --defline-qual '+' to avoid getting a second FASTQ header
# - The -F option gives original read names, but for some datasets this just
#   results in reads named 1, 2, 3 etc., so we use --defline-seq '@$ac.$si' to
#   get something slightly longer (and therefore more realistic).

# Do not delete the intermediate uncompressed files
.SECONDARY:

DATASETS = single43bp single9000bp paired150bp_1 paired150bp_2 paired300bp_1 paired300bp_2

all: $(foreach d,$(DATASETS),$(d).fastq.gz)

# 43 bp single-end, 11387212 reads
single43bp.fastq:
	fastq-dump -F --defline-qual '+' SRR020285
	mv SRR020285.fastq single43bp.fastq

# avg. length 9024 bp (PacBio), 115769 reads
single9000bp.fastq:
	fastq-dump --defline-seq '@$$ac.$$si' --defline-qual '+' SRR2174302
	mv SRR2174302.fastq single9000bp.fastq

# 2 x 150 bp paired-end, first 2 million reads
SRR12131341_1.fastq:
	fastq-dump --split-3 --maxSpotId 2000000 --defline-seq '@$$ac.$$si' --defline-qual '+' SRR12131341

# Both depend on the _1 version to work around make not being able to model two
# outputs in the fastq-dump rule
paired150bp_%.fastq: SRR12131341_1.fastq
	mv SRR12131341_$*.fastq $@

# 305 bp paired-end (MiSeq), 1380851 reads
ERR1760498_1.fastq:
	fastq-dump --split-3 -F --defline-qual '+' ERR1760498

paired300bp_%.fastq: ERR1760498_1.fastq
	mv ERR1760498_$*.fastq $@

# Fastq's gzipped with level 1. This is the most common gzip level for FASTQ files
# coming from sequencers.
%.fastq.gz: %.fastq
	gzip -k -1 $<
