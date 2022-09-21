#include "fastp/src/fastqreader.h"
#include "fastp/src/read.h"
#include "fastp/src/writer.h"
#include "fastp/src/options.h"
#include <stdio.h>
#include <mutex>

// fastp depends on these global variables
string command;
mutex logmtx;

int main(int argc, char* argv[]){
    if (argc != 3) {
        fprintf(stderr, "Input and output file must be given");
        return 1;
    }
    // fastp has its own xopen like functionality. This is actually the library
    // that is closest to dnaio in functionality despite the different 
    // languages. Quite cool!
    FastqReader reader = FastqReader(argv[1]);
    Options write_options = Options();
    Writer writer = Writer(&write_options, string(argv[2]), 0);
    Read *record;
    string record_str;
    while (1) {
        record = reader.read();
        if (record == NULL) {
            break;
        }
        writer.writeString(record->toString());
        delete record;
    }
    writer.flush();
    return 0;
}