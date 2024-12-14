"""
Day 12: Garden Groups --- Part One
https://adventofcode.com/2024/day/12
"""

import itertools
from collections import defaultdict


def merge_region(from_region, to_region, region_map):
    for row in range(len(region_map)):
        for col in range(len(region_map[row])):
            if region_map[row][col] == from_region:
                region_map[row][col] = to_region


def main():
    with open("input") as f:
        plot_map = tuple(tuple(c for c in r) for r in f.read().splitlines())

    region_map = []
    region_ids = itertools.count()

    for row in range(len(plot_map)):
        region_row = []
        region_map.append(region_row)

        for col in range(len(plot_map[row])):
            current_plot = plot_map[row][col]
            current_region = None

            if row > 0:
                up_plot = plot_map[row - 1][col]

                if current_plot == up_plot:
                    current_region = region_map[row - 1][col]

            if col > 0:
                left_plot = plot_map[row][col - 1]

                if current_plot == left_plot:
                    if current_region is None:
                        current_region = region_map[row][col - 1]
                    else:
                        left_region = region_map[row][col - 1]
                        merge_region(left_region, current_region, region_map)

            if current_region is None:
                current_region = next(region_ids)

            region_row.append(current_region)

    areas = defaultdict(int)
    perimeters = defaultdict(int)

    for row in range(len(region_map)):
        for col in range(len(region_map[row])):
            current_region = region_map[row][col]
            areas[current_region] += 1

            if row == 0 or region_map[row - 1][col] != current_region:
                perimeters[current_region] += 1

            if row == len(region_map) - 1 or region_map[row + 1][col] != current_region:
                perimeters[current_region] += 1

            if col == 0 or region_map[row][col - 1] != current_region:
                perimeters[current_region] += 1

            if (
                col == len(region_map[row]) - 1
                or region_map[row][col + 1] != current_region
            ):
                perimeters[current_region] += 1

    fence_cost = 0

    for region_id in areas:
        fence_cost += areas[region_id] * perimeters[region_id]

    print(fence_cost)


if __name__ == "__main__":
    main()
