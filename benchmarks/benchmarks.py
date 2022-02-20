import os
import dnaio
import io

try:
    dnaio.Sequence
except AttributeError:
    # Missing before v0.2
    dnaio.Sequence = dnaio._core.Sequence


def data_path(name):
    return os.path.join(os.environ["ASV_CONF_DIR"], "data", name) + ".fastq"


def time_parse_single(dataset):
    with dnaio.open(data_path(dataset)) as f:
        for record in f:
            pass


time_parse_single.params = [
    "single43bp", "paired150bp_1", "paired300bp_1", "single9000bp"
]
time_parse_single.param_names = ["singleend"]


def time_parse_paired(dataset):
    with dnaio.open(
        data_path(dataset + "_1"),
        file2=data_path(dataset + "_2"),
    ) as f:
        for record in f:
            pass

time_parse_paired.params = [
    "paired150bp", "paired300bp"
]
time_parse_paired.param_names = ["paired"]


class EmptyRecords:
    def setup(self):
        self.bytes_io = io.BytesIO(b"@\n\n+\n\n" * 10_000_000)

    def time_parse_empty_records(self):
        with dnaio.open(self.bytes_io) as f:
            for record in f:
                pass


class Suite:
    def setup(self):
        self.record = dnaio.Sequence("record_name", "ACGT" * 25, "=->!" * 25)

    def time_sequence_attribute(self):
        r = self.record
        for _ in range(1_000_000):
            r.sequence
