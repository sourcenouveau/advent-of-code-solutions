# Advent of Code Solutions: Day 1, part 2
# https://github.com/emddudley/advent-of-code-solutions

with open("input", "r") as input:
    instructions = input.read()

floor = 0
position = 0
underground = False

for instruction in instructions:
    position += 1

    if instruction == "(":
        floor += 1
    elif instruction == ")":
        floor -= 1

    if floor < 0:
        underground = True
        break

if underground:
    print(position)
else:
    print("Error: Santa never went underground.")
