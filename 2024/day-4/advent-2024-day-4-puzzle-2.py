"""
Day 4: Ceres Search --- Part Two
https://adventofcode.com/2024/day/4
"""


def scan(row, col, row_origin, col_origin, puzzle) -> bool:
    if not 1 <= row < len(puzzle) - 1:
        return False

    if not 1 <= col < len(puzzle[0]) - 1:
        return False

    row_dir = 0 if row_origin == col_origin else col_origin
    col_dir = 0 if row_origin != col_origin else -row_origin

    m1_row = row + row_origin
    m1_col = col + col_origin
    m2_row = m1_row + 2 * row_dir
    m2_col = m1_col + 2 * col_dir
    s1_row = row - row_origin
    s1_col = col - col_origin
    s2_row = s1_row - 2 * row_dir
    s2_col = s1_col - 2 * col_dir

    return (
        puzzle[m1_row][m1_col] == "M"
        and puzzle[m2_row][m2_col] == "M"
        and puzzle[s1_row][s1_col] == "S"
        and puzzle[s2_row][s2_col] == "S"
    )


def main():
    with open("input") as f:
        puzzle = f.read().splitlines()

    count = 0

    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] != "A":
                continue

            for row_origin, col_origin in (
                (-1, -1),
                (-1, 1),
                (1, 1),
                (1, -1),
            ):
                if scan(row, col, row_origin, col_origin, puzzle):
                    count += 1
                    break

    print(count)


if __name__ == "__main__":
    main()
