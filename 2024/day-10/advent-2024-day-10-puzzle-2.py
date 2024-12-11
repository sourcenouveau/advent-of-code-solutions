"""
Day 10: Hoof It --- Part Two
https://adventofcode.com/2024/day/10
"""


def trailheads(topo_map):
    for row in range(len(topo_map)):
        for col in range(len(topo_map[0])):
            if topo_map[row][col] == 0:
                yield row, col


def find_rating(row, col, topo_map):
    current_height = topo_map[row][col]

    if current_height == 9:
        return 1

    rating = 0
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

    for row_dir, col_dir in directions:
        next_row = row + row_dir
        next_col = col + col_dir

        if not 0 <= next_row < len(topo_map) or not 0 <= next_col < len(topo_map[0]):
            continue

        next_height = topo_map[next_row][next_col]

        if next_height != current_height + 1:
            continue

        rating += find_rating(next_row, next_col, topo_map)

    return rating


def main():
    with open("input") as f:
        topo_map = tuple(tuple(int(c) for c in r) for r in f.read().splitlines())

    total_rating = 0

    for row, col in trailheads(topo_map):
        total_rating += find_rating(row, col, topo_map)

    print(total_rating)


if __name__ == "__main__":
    main()
