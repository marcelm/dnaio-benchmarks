#include "fastp/src/fastqreader.h"
#include "fastp/src/read.h"
#include <stdio.h>
#include <mutex>

// fastp depends on these global variables
string command;
mutex logmtx;

int main(int argc, char* argv[]){
    if (argc != 3) {
        fprintf(stderr, "Two input files must be given");
        return 1;
    }
    char *forward_in = argv[1];
    char *reverse_in = argv[2];
    FastqReaderPair reader = FastqReaderPair(string(forward_in), string(reverse_in));

    ReadPair *record_pair;
    // Count records to verify reader works. Incrementing the integer shouldn't
    // slow down the program and dnaio also has a counter so it is not an
    // unfair addition.
    size_t records = 0;
    while (1) {
        record_pair = reader.read();
        if (record_pair == NULL) {
            fprintf(stderr, "counted %d records\n", records);
            return 0;
        }
        delete record_pair;
        records += 1;
    }
    return 0;
}
