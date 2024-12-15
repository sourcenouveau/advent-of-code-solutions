"""
Day 15: Warehouse Woes --- Part One
https://adventofcode.com/2024/day/15
"""

from collections import defaultdict


def print_map(warehouse_map):
    for i in range(len(warehouse_map)):
        print("".join(warehouse_map[i]))

    print()


def next_row_col(row, col, direction):
    if direction == "^":
        row_dir, col_dir = -1, 0
    elif direction == ">":
        row_dir, col_dir = 0, 1
    elif direction == "<":
        row_dir, col_dir = 0, -1
    elif direction == "v":
        row_dir, col_dir = 1, 0

    return row + row_dir, col + col_dir, row_dir, col_dir


def push_boxes(row, col, direction, warehouse_map):
    next_row, next_col, row_dir, col_dir = next_row_col(row, col, direction)

    if direction in ("<", ">"):
        next_box_col = next_col

        while True:
            if (
                not 0 <= next_row < len(warehouse_map)
                or not 0 <= next_box_col < len(warehouse_map[0])
                or warehouse_map[next_row][next_box_col] == "#"
            ):
                return row, col, 0, 0
            elif warehouse_map[next_row][next_box_col] in ("[", "]"):
                next_box_col = next_box_col + 2 * col_dir
            else:
                break

        next_box_col = next_col + col_dir

        while warehouse_map[next_row][next_box_col] in ("[", "]"):
            box_left = min(next_box_col, next_box_col + col_dir)
            box_right = max(next_box_col, next_box_col + col_dir)
            warehouse_map[next_row][box_left] = "["
            warehouse_map[next_row][box_right] = "]"
            next_box_col = next_box_col + 2 * col_dir
    else:
        box_row = next_row
        box_lefts_by_row = defaultdict(list)

        if warehouse_map[box_row][next_col] == "[":
            box_lefts_by_row[box_row].append(next_col)
        else:
            box_lefts_by_row[box_row].append(next_col - 1)

        while True:
            next_box_row = box_row + row_dir

            for box_left in box_lefts_by_row[box_row]:
                if (
                    warehouse_map[next_box_row][box_left] == "#"
                    or warehouse_map[next_box_row][box_left + 1] == "#"
                ):
                    return row, col, 0, 0

                if warehouse_map[next_box_row][box_left] == "[":
                    box_lefts_by_row[next_box_row].append(box_left)
                elif warehouse_map[next_box_row][box_left] == "]":
                    box_lefts_by_row[next_box_row].append(box_left - 1)

                if warehouse_map[next_box_row][box_left + 1] == "[":
                    box_lefts_by_row[next_box_row].append(box_left + 1)

            if not box_lefts_by_row[next_box_row]:
                break

            box_row = next_box_row

        for box_row, box_lefts in reversed(box_lefts_by_row.items()):
            for box_left in box_lefts:
                warehouse_map[box_row][box_left] = "."
                warehouse_map[box_row][box_left + 1] = "."
                warehouse_map[box_row + row_dir][box_left] = "["
                warehouse_map[box_row + row_dir][box_left + 1] = "]"

    return next_row, next_col, row_dir, col_dir


def next_position(row, col, direction, warehouse_map):
    next_row, next_col, row_dir, col_dir = next_row_col(row, col, direction)

    if not 0 <= next_row < len(warehouse_map) or not 0 <= next_col < len(
        warehouse_map[0]
    ):
        return row, col, 0, 0

    if warehouse_map[next_row][next_col] == ".":
        return next_row, next_col, row_dir, col_dir
    elif warehouse_map[next_row][next_col] == "#":
        return row, col, 0, 0
    else:
        return push_boxes(row, col, direction, warehouse_map)


def main():
    warehouse_map = []
    directions = ""

    with open("input") as f:
        for line in f:
            line = line.strip()

            if not line:
                break

            row = []

            for c in line:
                if c == "#":
                    row.extend(["#", "#"])
                elif c == "O":
                    row.extend(["[", "]"])
                elif c == ".":
                    row.extend([".", "."])
                elif c == "@":
                    row.extend(["@", "."])

            warehouse_map.append(row)

        for line in f:
            directions += line.strip()

    found_robot = False

    for row in range(len(warehouse_map)):
        for col in range(len(warehouse_map[0])):
            if warehouse_map[row][col] == "@":
                found_robot = True
                break

        if found_robot:
            break

    for direction in directions:
        warehouse_map[row][col] = direction

        # print_map(warehouse_map)
        # _ = input()

        next_row, next_col, row_dir, col_dir = next_position(
            row, col, direction, warehouse_map
        )

        if warehouse_map[next_row][next_col] == "O":
            box_row, box_col = next_row, next_col

            while warehouse_map[box_row][box_col] == "O":
                box_row, box_col = box_row + row_dir, box_col + col_dir

            warehouse_map[box_row][box_col] = "O"

        warehouse_map[row][col] = "."
        row, col = next_row, next_col

    gps_sum = 0

    for row in range(len(warehouse_map)):
        for col in range(len(warehouse_map[0])):
            if warehouse_map[row][col] == "[":
                gps_sum += 100 * row + col

    print(gps_sum)


if __name__ == "__main__":
    main()
