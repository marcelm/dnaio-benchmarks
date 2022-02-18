import os
import dnaio


def data_path(name):
    return os.path.join(os.environ["ASV_CONF_DIR"], "data", name)


def time_parse_SRR020285():
    with dnaio.open(data_path("SRR020285.fastq")) as f:
        for record in f:
            pass


def time_SRR020285_sequence_attribute():
    with dnaio.open(data_path("SRR020285.fastq")) as f:
        for record in f:
            len(record.sequence)
