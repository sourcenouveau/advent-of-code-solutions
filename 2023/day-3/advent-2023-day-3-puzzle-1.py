"""
Day 3: Gear Ratios --- Part One
https://adventofcode.com/2023/day/3
"""

from collections import namedtuple

SchematicNumber = namedtuple("SchematicNumber", "num_str row col_start")


def is_symbol(c):
    return c != "." and not c.isdigit()


def in_bounds(row, col, schematic):
    return 0 <= row <= len(schematic) - 1 and 0 <= col <= len(schematic[0]) - 1


def scan_adjacent(number, schematic):
    col_left = number.col_start - 1
    col_right = number.col_start + len(number.num_str) + 1

    row = number.row - 1

    for col in range(col_left, col_right):
        if in_bounds(row, col, schematic):
            yield row, col

    row = number.row
    col = number.col_start - 1

    if in_bounds(row, col, schematic):
        yield row, col

    col = number.col_start + len(number.num_str)

    if in_bounds(row, col, schematic):
        yield row, col

    row = number.row + 1

    for col in range(col_left, col_right):
        if in_bounds(row, col, schematic):
            yield row, col


def main():
    with open("input") as f:
        schematic = f.read().splitlines()

    numbers = []

    for row, line in enumerate(schematic):
        col_start = 0
        num_str = ""

        for col, char in enumerate(line):
            if char.isdigit():
                if not num_str:
                    col_start = col

                num_str += char
            else:
                if num_str:
                    numbers.append(SchematicNumber(num_str, row, col_start))

                num_str = ""

        if num_str:
            numbers.append(SchematicNumber(num_str, row, col_start))

    number_sum = 0

    for number in numbers:
        for row, col in scan_adjacent(number, schematic):
            if is_symbol(schematic[row][col]):
                number_sum += int(number.num_str)
                break

    print(number_sum)


if __name__ == "__main__":
    main()
