#include "fastp/src/fastqreader.h"
#include "fastp/src/read.h"
#include <stdio.h>
#include <mutex>

// fastp depends on these global variables
string command;
mutex logmtx;

int main(int argc, char* argv[]){
    if (argc != 2) {
        fprintf(stderr, "Input file must be given");
        return 1;
    }
    char *in_file = argv[1];
    FastqReader reader = FastqReader(in_file);
    Read *record;
    // Count records to verify reader works. Incrementing the integer shouldn't
    // slow down the program and dnaio also has a counter so it is not an
    // unfair addition.
    size_t records = 0;
    while (1) {
        record = reader.read();
        if (record == NULL) {
            fprintf(stderr, "counted %d records\n", records);
            return 0;
        }
        records += 1;
    }
    return 0;
}