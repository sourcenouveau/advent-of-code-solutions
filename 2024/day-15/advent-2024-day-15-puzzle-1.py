"""
Day 15: Warehouse Woes --- Part One
https://adventofcode.com/2024/day/15
"""


def next_position(row, col, direction, warehouse_map):
    if direction == "^":
        row_dir, col_dir = -1, 0
    elif direction == ">":
        row_dir, col_dir = 0, 1
    elif direction == "<":
        row_dir, col_dir = 0, -1
    elif direction == "v":
        row_dir, col_dir = 1, 0

    next_row, next_col = row + row_dir, col + col_dir

    if not 0 <= next_row < len(warehouse_map) or not 0 <= next_col < len(
        warehouse_map[0]
    ):
        return row, col, 0, 0

    if warehouse_map[next_row][next_col] == "#":
        return row, col, 0, 0

    next_box_row, next_box_col = next_row, next_col

    while True:
        if not 0 <= next_box_row < len(warehouse_map) or not 0 <= next_box_col < len(
            warehouse_map[0]
        ):
            return row, col, 0, 0
        elif warehouse_map[next_box_row][next_box_col] == "O":
            next_box_row, next_box_col = next_box_row + row_dir, next_box_col + col_dir
        elif warehouse_map[next_box_row][next_box_col] == "#":
            return row, col, 0, 0
        else:
            break

    return next_row, next_col, row_dir, col_dir


def main():
    warehouse_map = []
    directions = ""

    with open("input") as f:
        for line in f:
            line = line.strip()

            if not line:
                break

            warehouse_map.append([c for c in line])

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
            if warehouse_map[row][col] == "O":
                gps_sum += 100 * row + col

    print(gps_sum)


if __name__ == "__main__":
    main()
