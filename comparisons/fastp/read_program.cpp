#include "fastp/src/fastqreader.h"
#include "fastp/src/read.h"
#include <stdio.h>
#include <mutex>

// fastp depends on these global variables
string command;
mutex logmtx;

int main(int argc, char* argv[]){
    if (argc != 1) {
        fprintf(stderr, "Input file must be given");
        return 1;
    }
    char *in_file = argv[0];
    FastqReader reader = FastqReader(in_file);
    Read *record;
    while (1) {
        record = reader.read();
        if (record == NULL) {
            return 0;
        }
    }
    return 0;
}