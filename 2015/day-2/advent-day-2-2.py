# Advent of Code Solutions: Day 2, part 2
# https://github.com/emddudley/advent-of-code-solutions

with open("input", "r") as input:
    dimensions_list = input.read().splitlines()

total_length = 0

for dimensions in dimensions_list:
    lwh = sorted(map(int, dimensions.split("x")))
    ribbon = 2 * lwh[0] + 2 * lwh[1]
    bow = lwh[0] * lwh[1] * lwh[2]
    total_length += ribbon + bow

print(total_length)
