# Advent of Code Solutions: Day 3, part 2
# https://github.com/emddudley/advent-of-code-solutions

def parse_direction(current_location, direction):
    if direction == '^': current_location[1] += 1
    elif direction == '>': current_location[0] += 1
    elif direction == 'v': current_location[1] -= 1
    elif direction == '<': current_location[0] -= 1
    else: print("Error parsing direction '%s'" % direction)
    return current_location

with open('input', 'r') as input:
    directions = input.read()

houses = {}
actor = 0
current = [[0, 0], [0, 0]]

for direction in directions:
    coordinates = str(current[actor])
    if coordinates not in houses:
        houses[coordinates] = 0
    houses[coordinates] += 1
    current[actor] = parse_direction(current[actor], direction)
    actor = (actor + 1) % len(current)

print(len(houses))
