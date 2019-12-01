# Advent of Code Solutions: Day 8, part 2
# https://github.com/emddudley/advent-of-code-solutions

code = 0
enc = 0

with open('input', 'r') as f:
    for line in f:
        code += len(line) - 1
        enc += len(line) - 1 + 2 + line.count("\"") + line.count("\\")

print(enc - code)
