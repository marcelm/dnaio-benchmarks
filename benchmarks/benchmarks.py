import os
import dnaio


def data_path(name):
    return os.path.join(os.environ["ASV_CONF_DIR"], "data", name)


def time_parse_single_43bp(path):
    with dnaio.open(path) as f:
        for record in f:
            pass


time_parse_single_43bp.params = [
    data_path(path + ".fastq") for path in
    ["single43bp", "paired150bp_1", "paired300bp_1", "single9000bp"]
]
time_parse_single_43bp.param_names = ["dataset"]


class Suite:
    def setup(self):
        self.record = dnaio.Sequence("record_name", "ACGT" * 25, "=->!" * 25)

    def time_sequence_attribute(self):
        r = self.record
        for _ in range(100_000):
            r.sequence
