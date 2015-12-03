# Advent of Code Solutions: Day 3, part 1
# https://github.com/emddudley/advent-of-code-solutions

with open('input', 'r') as input:
    directions = input.read()

houses = {}
current = [0, 0]

for direction in directions:
    if str(current) not in houses:
        houses[str(current)] = 0

    houses[str(current)] += 1

    if direction == '^':
        current[1] += 1
    elif direction == '>':
        current[0] += 1
    elif direction == 'v':
        current[1] -= 1
    elif direction == '<':
        current[0] -= 1
    else:
        print("Error parsing direction '%s'" % direction)

print(len(houses))
