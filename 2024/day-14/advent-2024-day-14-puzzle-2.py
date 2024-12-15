"""
Day 14: Restroom Redoubt --- Part Two
https://adventofcode.com/2024/day/14
"""

import re


def main():
    w = 101
    h = 103

    robots = []

    with open("input") as f:
        for line in f:
            px, py, vx, vy = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line).groups()
            robots.append([int(px), int(py), int(vx), int(vy)])

    elapsed = 0

    while True:
        robot_map = [["."] * w for _ in range(h)]

        for r in robots:
            robot_map[r[1]][r[0]] = "#"

        print_it = False

        for row in robot_map:
            if "##########" in "".join(row):
                print_it = True
                break

        if print_it:
            for row in robot_map:
                print("".join(row))

            break

        for r in robots:
            r[0] = (r[0] + r[2]) % w
            r[1] = (r[1] + r[3]) % h

        elapsed += 1

    print(elapsed)


if __name__ == "__main__":
    main()
