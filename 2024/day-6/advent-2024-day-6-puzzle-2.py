"""
Day 6: Guard Gallivant --- Part Two
https://adventofcode.com/2024/day/6
"""

import time

GUARD_DIRS = ("^", ">", "v", "<")


def in_lab(guard_row, guard_col, lab_map):
    return 0 <= guard_row < len(lab_map) and 0 <= guard_col < len(lab_map[0])


def next_look_row_col(guard_row, guard_col, guard_dir):
    if guard_dir == "^":
        next_row = guard_row - 1
        next_col = guard_col
    elif guard_dir == ">":
        next_row = guard_row
        next_col = guard_col + 1
    elif guard_dir == "v":
        next_row = guard_row + 1
        next_col = guard_col
    elif guard_dir == "<":
        next_row = guard_row
        next_col = guard_col - 1
    else:
        raise Exception(f"unknown guard direction {guard_dir}")
    
    return next_row, next_col


def turn_dir(guard_dir):
    return GUARD_DIRS[(GUARD_DIRS.index(guard_dir) + 1) % len(GUARD_DIRS)]


def guard_next(guard_row, guard_col, guard_dir, lab_map):
    next_row, next_col = next_look_row_col(guard_row, guard_col, guard_dir)
    still_in_lab = in_lab(next_row, next_col, lab_map)

    if still_in_lab and lab_map[next_row][next_col] == "#":
        guard_dir = turn_dir(guard_dir)
    else:
        guard_row = next_row
        guard_col = next_col

    return guard_row, guard_col, guard_dir


def explore(guard_row, guard_col, guard_dir, lab_map):
    explored = set()

    while in_lab(guard_row, guard_col, lab_map):
        current = (guard_row, guard_col, guard_dir)

        if current in explored:
            return 'loop'

        explored.add(current)
        guard_row, guard_col, guard_dir = guard_next(guard_row, guard_col, guard_dir, lab_map)

    return 'exit'


def main():
    with open("input") as f:
        lab_map = list(list(col for col in row.strip()) for row in f.readlines())

    guard_row = None
    guard_col = None
    guard_dir = None

    for row in range(len(lab_map)):
        for col in range(len(lab_map[row])):
            if lab_map[row][col] in GUARD_DIRS:
                guard_row = row
                guard_col = col
                guard_dir = lab_map[row][col]
                break

        if guard_dir:
            break
    else:
        raise Exception("guard not found")

    explored = set()
    obstructions = set()

    while in_lab(guard_row, guard_col, lab_map):
        explored.add((guard_row, guard_col))
        obs_row, obs_col = next_look_row_col(guard_row, guard_col, guard_dir)

        if in_lab(obs_row, obs_col, lab_map) and (obs_row, obs_col) not in explored:
            prev_item = lab_map[obs_row][obs_col]

            if prev_item != "#":
                lab_map[obs_row][obs_col] = "#"

                if explore(guard_row, guard_col, guard_dir, lab_map) == 'loop':
                    obstructions.add((obs_row, obs_col))

                lab_map[obs_row][obs_col] = prev_item

        guard_row, guard_col, guard_dir = guard_next(guard_row, guard_col, guard_dir, lab_map)

    print(len(obstructions))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f'Took {round(end - start, 1)} seconds')
