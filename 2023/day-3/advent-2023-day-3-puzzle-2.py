"""
Day 3: Gear Ratios --- Part Two
https://adventofcode.com/2023/day/3
"""

from collections import namedtuple

SchematicNumber = namedtuple("SchematicNumber", "num_str row col_start")


def in_bounds(row, col, schematic):
    return 0 <= row <= len(schematic) - 1 and 0 <= col <= len(schematic[0]) - 1


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

    numbers_by_row = [[] for _ in schematic]

    for number in numbers:
        numbers_by_row[number.row].append(number)

    gear_ratio_sum = 0

    for row, line in enumerate(schematic):
        for col, char in enumerate(line):
            if char == "*":
                adjacent = []

                check_row = row - 1

                if 0 <= check_row <= len(schematic) - 1:
                    for number in numbers_by_row[check_row]:
                        if (
                            col - 1 <= number.col_start <= col + 1
                            or col - 1
                            <= number.col_start + len(number.num_str) - 1
                            <= col + 1
                        ):
                            adjacent.append(number)

                check_row = row

                for number in numbers_by_row[check_row]:
                    if number.col_start + len(number.num_str) - 1 == col - 1:
                        adjacent.append(number)
                    elif number.col_start == col + 1:
                        adjacent.append(number)

                check_row = row + 1

                if 0 <= check_row <= len(schematic) - 1:
                    for number in numbers_by_row[check_row]:
                        if (
                            col - 1 <= number.col_start <= col + 1
                            or col - 1
                            <= number.col_start + len(number.num_str) - 1
                            <= col + 1
                        ):
                            adjacent.append(number)

                if len(adjacent) == 2:
                    gear_ratio_sum += int(adjacent[0].num_str) * int(
                        adjacent[1].num_str
                    )

    print(gear_ratio_sum)


if __name__ == "__main__":
    main()
