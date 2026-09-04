CXX := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -Wpedantic

.PHONY: all run clean

all: rpg_core

rpg_core: main.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

run: rpg_core
	python3 rpg_gui.py

clean:
	rm -f rpg_core
