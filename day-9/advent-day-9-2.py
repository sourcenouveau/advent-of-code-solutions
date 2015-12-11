# Advent of Code Solutions: Day 9, part 2
# https://github.com/emddudley/advent-of-code-solutions

import itertools

distances = {}

with open('input', 'r') as f:
    for line in f:
        tokens = line.split(' ')
        fromloc = tokens[0]
        toloc = tokens[2]
        distance = tokens[4]

        if not fromloc in distances:
            distances[fromloc] = {}

        if not toloc in distances:
            distances[toloc] = {}

        distances[fromloc][toloc] = int(distance)
        distances[toloc][fromloc] = int(distance)

routes = itertools.permutations(distances.keys())
routelengths = []

for route in routes:
    routelength = 0

    for i in range(0, len(route) - 1):
        routelength += distances[route[i]][route[i + 1]]

    routelengths.append(routelength)

print(max(routelengths))
