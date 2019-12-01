# Advent of Code Solutions: Day 8, part 1
# https://github.com/emddudley/advent-of-code-solutions

code = 0
mem = 0

with open('input', 'r') as f:
    for line in f:
        code += len(line) - 1
        mem += len(line.decode("string-escape")) - 3

print(code - mem)
