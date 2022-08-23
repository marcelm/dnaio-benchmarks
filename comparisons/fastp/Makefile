FASTP_SRC := ./fastp/src

FASTP_FILES := ${FASTP_SRC}/fastqreader.cpp ${FASTP_SRC}/read.cpp ${FASTP_SRC}/readpool.cpp \
	${FASTP_SRC}/options.cpp
OBJ := $(patsubst %.cpp,${DIR_OBJ}/%.o,$(notdir ${SRC}))

CXX := g++
CXX_FLAGS := -std=c++11 -pthread -g -O3 ${CXXFLAGS}
LIBS := -lisal -ldeflate -lpthread
LD_FLAGS := $(foreach librarydir,$(LIBRARY_DIRS),-L$(librarydir)) $(LIBS) $(LD_FLAGS)

