"""
Day 4: Ceres Search --- Part One
https://adventofcode.com/2024/day/4
"""


def scan(row, col, row_step, col_step, puzzle) -> bool:
    if not 0 <= row + 3 * row_step < len(puzzle):
        return False

    if not 0 <= col + 3 * col_step < len(puzzle[0]):
        return False

    return (
        puzzle[row + 1 * row_step][col + 1 * col_step] == "M"
        and puzzle[row + 2 * row_step][col + 2 * col_step] == "A"
        and puzzle[row + 3 * row_step][col + 3 * col_step] == "S"
    )


def main():
    with open("input") as f:
        puzzle = f.read().splitlines()

    count = 0

    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] != "X":
                continue

            for row_step, col_step in (
                (0, 1),
                (1, 1),
                (1, 0),
                (1, -1),
                (0, -1),
                (-1, -1),
                (-1, 0),
                (-1, 1),
            ):
                if scan(row, col, row_step, col_step, puzzle):
                    count += 1

    print(count)


if __name__ == "__main__":
    main()
