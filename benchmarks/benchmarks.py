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


def time_parse_single(dataset, mode):
    with dnaio.open(data_path(dataset), mode=mode) as f:
        for record in f:
            pass


FASTQ_FILES = [
    "single43bp", "paired150bp_1", "paired300bp_1", "single9000bp"
]
MODES = ["r"]
if hasattr(dnaio, "BytesSequence"):
    MODES.append("rb")

time_parse_single.params = (FASTQ_FILES, MODES)
time_parse_single.param_names = ["singleend", "mode"]


def time_parse_paired(dataset, mode):
    with dnaio.open(
        data_path(dataset + "_1"),
        file2=data_path(dataset + "_2"),
        mode=mode,
    ) as f:
        for record in f:
            pass


PAIRED_FASTQ_FILES = ["paired150bp", "paired300bp"]
time_parse_paired.params = (PAIRED_FASTQ_FILES, MODES)
time_parse_paired.param_names = ["paired", "mode"]


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
