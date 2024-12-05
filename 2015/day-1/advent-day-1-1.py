# Advent of Code Solutions: Day 1, part 1
# https://github.com/emddudley/advent-of-code-solutions

with open("input", "r") as input:
    instructions = input.read()
    print(instructions.count("(") - instructions.count(")"))
