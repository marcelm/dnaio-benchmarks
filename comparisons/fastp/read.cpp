#include "fastp/src/fastqreader.h"
#include <errno.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Input and output file must be given");
        return 1;
    }
    char *in_file = argv[0];
    char *out_file = argv[1];
}