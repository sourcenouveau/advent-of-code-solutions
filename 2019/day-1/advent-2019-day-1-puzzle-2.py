# Advent of Code 2019 Solutions: Day 1, Puzzle 2
# https://github.com/emddudley/advent-of-code-solutions


def fuel(mass: int) -> int:
    if mass <= 0:
        return 0

    fuel_mass = max(0, int(mass / 3) - 2)

    return fuel_mass + fuel(fuel_mass)


total_fuel = 0

with open('input', 'r') as f:
    for line in f:
        mass = int(line)
        total_fuel += fuel(mass)

print(total_fuel)
