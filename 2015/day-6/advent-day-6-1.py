# Advent of Code Solutions: Day 6, part 1
# https://github.com/emddudley/advent-of-code-solutions

import re


def twinkle_lights(instruction, lights):
    tokens = re.split(r"(\d+)", instruction)
    operation = tokens[0].strip()

    if operation == "turn on":
        twinkle = lambda x: True
    elif operation == "turn off":
        twinkle = lambda x: False
    elif operation == "toggle":
        twinkle = lambda x: not x
    else:
        twinkle = lambda x: x

    coord_1 = [int(tokens[1]), int(tokens[3])]
    coord_2 = [int(tokens[5]), int(tokens[7])]

    for x in range(coord_1[0], coord_2[0] + 1):
        for y in range(coord_1[1], coord_2[1] + 1):
            lights[x][y] = twinkle(lights[x][y])


lights = [[False] * 1000 for n in range(1000)]

with open("input", "r") as input:
    for instruction in input:
        twinkle_lights(instruction, lights)

print(sum(map(sum, lights)))
