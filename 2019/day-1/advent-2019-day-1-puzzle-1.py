# Advent of Code 2019 Solutions: Day 1, Puzzle 1
# https://github.com/emddudley/advent-of-code-solutions


def fuel(mass: int) -> int:
    return int(mass / 3) - 2


total_fuel = 0

with open("input", "r") as f:
    for line in f:
        mass = int(line)
        total_fuel += fuel(mass)

print(total_fuel)
