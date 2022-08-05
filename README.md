# Benchmark results

[Benchmarks](https://marcelm.github.io/dnaio-benchmarks/) for [dnaio](https://github.com/marcelm/dnaio)

# Download benchmarking datasets

    conda create -n sratools sra-tools
    cd data
    ./download.sh

# Airspeed Velocity (asv)

Some benchmarks are run using [airspeed velocity](http://github.com/airspeed-velocity/asv/).
They are currently run manually on a rented virtual machine somewhere on the internet,
so the measurements are not as reliable as they would be on a dedicated machine.

    python3 -m venv .venv
    source .venv/bin/activate
    pip install asv

To run this, the benchmarking datasets need to be downloaded first. Ensure you have `fastq-dump` available, then run `cd data && ./download.sh` to do so.

Run benchmarks with:

    asv run -k

Publish:

    asv gh-pages


# Running library comparisons

Ensure benchmark data was downloaded as described above.

    conda create -n dnaio-benchmarks python sra-tools
    conda activate dnaio-benchmarks
    grep '^# pip install' comparelibs.py | cut -c15- | xargs pip install  # This is the worst way to do it
    python ./comparelibs.py
