import os
import dnaio


def data_path(name):
    return os.path.join(os.environ["ASV_CONF_DIR"], "data", name) + ".fastq"


def time_parse_single(dataset):
    with dnaio.open(data_path(dataset)) as f:
        for record in f:
            pass


time_parse_single.params = [
    "single43bp", "paired150bp_1", "paired300bp_1", "single9000bp"
]
time_parse_single.param_names = ["dataset"]


def time_parse_paired(path):
    with dnaio.open(
        data_path(path + "_1"),
        file2=data_path(path + "_2"),
    ) as f:
        for record in f:
            pass

time_parse_paired.params = [
    "paired150bp", "paired300bp"
]
time_parse_single.param_names = ["dataset"]


class Suite:
    def setup(self):
        self.record = dnaio.Sequence("record_name", "ACGT" * 25, "=->!" * 25)

    def time_sequence_attribute(self):
        r = self.record
        for _ in range(1_000_000):
            r.sequence
