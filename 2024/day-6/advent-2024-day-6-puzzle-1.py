"""
Day 6: Guard Gallivant --- Part One
https://adventofcode.com/2024/day/6
"""


def main():
    with open("input") as f:
        lab_map = f.read().splitlines()

    guard_dirs = ("^", ">", "v", "<")

    guard_row = None
    guard_col = None
    guard_dir = None

    for row in range(len(lab_map)):
        for col in range(len(lab_map[row])):
            if lab_map[row][col] in guard_dirs:
                guard_row = row
                guard_col = col
                guard_dir = lab_map[row][col]
                break

        if guard_dir:
            break
    else:
        raise Exception("guard not found")

    positions = set()

    while 0 <= guard_row < len(lab_map) and 0 <= guard_col < len(lab_map[0]):
        positions.add((guard_row, guard_col))

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

        if lab_map[next_row][next_col] == "#":
            guard_dir = guard_dirs[(guard_dirs.index(guard_dir) + 1) % len(guard_dirs)]
        else:
            guard_row = next_row
            guard_col = next_col

    print(len(positions))


if __name__ == "__main__":
    main()
