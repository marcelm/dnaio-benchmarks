DIR_INC := ./inc
FASTP_DIR_SRC := ./fastp/src
DIR_OBJ := ./obj

PREFIX ?= /usr/local
BINDIR ?= $(PREFIX)/bin
INCLUDE_DIRS ?=
LIBRARY_DIRS ?=

FASTP_SRC := $(wildcard ${FASTP_DIR_SRC}/*.cpp)
FASTP_OBJ := $(patsubst %.cpp,${DIR_OBJ}/%.o,$(notdir ${FASTP_SRC}))

TARGET := all

CXX ?= g++
CXXFLAGS := -std=c++11 -pthread -g -O3 -I${DIR_INC} $(foreach includedir,$(INCLUDE_DIRS),-I$(includedir)) ${CXXFLAGS}
LIBS := -lisal -ldeflate -lpthread
STATIC_FLAGS := -static -Wl,--no-as-needed -pthread
LD_FLAGS := $(foreach librarydir,$(LIBRARY_DIRS),-L$(librarydir)) $(LIBS) $(LD_FLAGS)
STATIC_LD_FLAGS := $(foreach librarydir,$(LIBRARY_DIRS),-L$(librarydir)) $(STATIC_FLAGS) $(LIBS) $(STATIC_LD_FLAGS)

all: read.py read_and_write.py read_program read_and_write_program read_paired_program read_paired.py

%.py:%_program
	ln -fs $*_program $*.py

./%_program:./%_program.o ${FASTP_OBJ}
	$(CXX) $(FASTP_OBJ) ./$*_program.o -o $*_program $(LD_FLAGS)

static:${FASTP_OBJ}
	$(CXX) $(FASTP_OBJ) -o ${BIN_TARGET} $(STATIC_LD_FLAGS)

./%.o:./%.cpp
	$(CXX) -c $< -o $@ $(CXXFLAGS)

${DIR_OBJ}/%.o:${FASTP_DIR_SRC}/%.cpp make_obj_dir
	$(CXX) -c $< -o $@ $(CXXFLAGS)

.PHONY:clean
.PHONY:static
.PHONY:all$(notdir ${SRC})
clean:
	@if test -d $(DIR_OBJ) ; \
	then \
		find $(DIR_OBJ) -name *.o -delete; \
	fi
	@if test -e $(TARGET) ; \
	then \
		rm $(TARGET) ; \
	fi

make_obj_dir:
	@if test ! -d $(DIR_OBJ) ; \
	then \
		mkdir $(DIR_OBJ) ; \
	fi

install:
	install $(TARGET) $(BINDIR)/$(TARGET)
	@echo "Installed."
