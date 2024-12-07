"""
Day 3: Mull It Over --- Part Two
https://adventofcode.com/2024/day/3
"""

import re


def main():
    with open("input") as f:
        memory = ''.join(f.readlines())

    result = 0
    active = True

    for p in range(len(memory)):
        window = memory[p:p + 20]

        if window.startswith("do()"):
            active = True
        elif window.startswith("don't()"):
            active = False
        elif m := re.match(r"mul\((\d+),(\d+)\)", window):
            if active:
                x, y = m.group(1, 2)
                result += int(x) * int(y)

    print(result)


if __name__ == "__main__":
    main()
