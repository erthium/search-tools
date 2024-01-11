CC := g++
CFLAGS := -Wall -std=c++11 -Iinclude
LDFLAGS := -Llib -l:libutf8proc.a

SRC_DIR := src
OBJ_DIR := build
BIN_DIR := bin

SRC := $(wildcard $(SRC_DIR)/*.cpp)
OBJ := $(patsubst $(SRC_DIR)/%.cpp, $(OBJ_DIR)/%.o, $(SRC))
EXECUTABLE := $(BIN_DIR)/search.smart

.PHONY: all clean run

all: clean $(EXECUTABLE)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -c $< -o $@

$(EXECUTABLE): $(OBJ)
	$(CC) $^ -o $@ $(LDFLAGS)

clean:
	rm -f $(OBJ_DIR)/*.o $(BIN_DIR)/*

run: $(EXECUTABLE)
	./$(EXECUTABLE)
