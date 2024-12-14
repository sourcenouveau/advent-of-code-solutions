"""
Day 12: Garden Groups --- Part Two
https://adventofcode.com/2024/day/12
"""

import itertools
from collections import defaultdict


TOP = 0
BOTTOM = 1
LEFT = 2
RIGHT = 3


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
    perimeters = defaultdict(lambda: defaultdict(set))

    for row in range(len(region_map)):
        for col in range(len(region_map[row])):
            current_region = region_map[row][col]
            areas[current_region] += 1

            if row == 0 or region_map[row - 1][col] != current_region:
                perimeters[current_region][TOP].add((row, col))

            if row == len(region_map) - 1 or region_map[row + 1][col] != current_region:
                perimeters[current_region][BOTTOM].add((row, col))

            if col == 0 or region_map[row][col - 1] != current_region:
                perimeters[current_region][LEFT].add((row, col))

            if (
                col == len(region_map[row]) - 1
                or region_map[row][col + 1] != current_region
            ):
                perimeters[current_region][RIGHT].add((row, col))

    sides = defaultdict(int)

    for region, perimeter in perimeters.items():
        side_count = 0

        top_cols_by_row = defaultdict(set)

        for row, col in perimeter[TOP]:
            top_cols_by_row[row].add(col)

        for row, cols in top_cols_by_row.items():
            prev_col = None

            for col in sorted(cols):
                if prev_col is None or prev_col + 1 != col:
                    side_count += 1

                prev_col = col

        bottom_cols_by_row = defaultdict(set)

        for row, col in perimeter[BOTTOM]:
            bottom_cols_by_row[row].add(col)

        for row, cols in bottom_cols_by_row.items():
            prev_col = None

            for col in sorted(cols):
                if prev_col is None or prev_col + 1 != col:
                    side_count += 1

                prev_col = col

        left_rows_by_col = defaultdict(set)

        for row, col in perimeter[LEFT]:
            left_rows_by_col[col].add(row)

        for col, rows in left_rows_by_col.items():
            prev_row = None

            for row in sorted(rows):
                if prev_row is None or prev_row + 1 != row:
                    side_count += 1

                prev_row = row

        right_rows_by_col = defaultdict(set)

        for row, col in perimeter[RIGHT]:
            right_rows_by_col[col].add(row)

        for col, rows in right_rows_by_col.items():
            prev_row = None

            for row in sorted(rows):
                if prev_row is None or prev_row + 1 != row:
                    side_count += 1

                prev_row = row

        sides[region] = side_count

    fence_cost = 0

    for region_id in areas:
        fence_cost += areas[region_id] * sides[region_id]

    print(fence_cost)


if __name__ == "__main__":
    main()
