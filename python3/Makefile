PY := python3
FLAGS := -b
SRC_DIR := .
TESTS_DIR := tests

MAIN_SCRIPT := $(SRC_DIR)/main.py
TEST_SCRIPT := $(TESTS_DIR)/general_tests.py


.PHONY: test clean run


test:
	$(PY) $(FLAGS) $(TEST_SCRIPT)


clean:
	rm -rf $(SRC_DIR)/__pycache__ $(TESTS_DIR)/__pycache__


run:
	$(PY) $(FLAGS) $(MAIN_SCRIPT)
