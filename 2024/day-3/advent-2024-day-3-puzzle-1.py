"""
Day 3: Mull It Over --- Part One
https://adventofcode.com/2024/day/3
"""

import re


def main():
    result = 0

    with open("input") as f:
        for line in f:
            result += sum(
                int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", line)
            )

    print(result)


if __name__ == "__main__":
    main()
