"""
Day 8: Resonant Collinearity --- Part Two
https://adventofcode.com/2024/day/8
"""

import itertools


def main():
    with open("input") as f:
        antenna_map = tuple(tuple(c for c in r) for r in f.read().splitlines())

    map_rows = len(antenna_map)
    map_cols = len(antenna_map[0])

    antennas = {}

    for row in range(map_rows):
        for col in range(map_cols):
            frequency = antenna_map[row][col]
            
            if not frequency.isalnum():
                continue
            
            if frequency not in antennas:
                antennas[frequency] = []

            antennas[frequency].append((row, col))

    antinodes = set()

    for frequency, locations in antennas.items():
        for ant_1, ant_2 in itertools.permutations(locations, 2):
            dist_rows = ant_2[0] - ant_1[0]
            dist_cols = ant_2[1] - ant_1[1]

            antinode_row = ant_1[0]
            antinode_col = ant_1[1]

            while 0 <= antinode_row < map_rows and 0 <= antinode_col < map_cols:
                antinodes.add((antinode_row, antinode_col))
                antinode_row += dist_rows
                antinode_col += dist_cols

            antinode_row = ant_1[0]
            antinode_col = ant_1[1]

            while 0 <= antinode_row < map_rows and 0 <= antinode_col < map_cols:
                antinodes.add((antinode_row, antinode_col))
                antinode_row -= dist_rows
                antinode_col -= dist_cols
    
    print(len(antinodes))


if __name__ == "__main__":
    main()
