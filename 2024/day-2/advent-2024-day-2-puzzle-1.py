"""
Day 2: Red-Nosed Reports --- Part One
https://adventofcode.com/2024/day/2
"""

import operator
from itertools import pairwise


def main():
    safe_reports = 0

    with open("input") as f:
        for report in f.readlines():
            levels = list(map(int, report.split(" ")))

            compare = operator.lt if levels[0] < levels[1] else operator.gt
            is_safe = all(
                compare(l1, l2) and abs(l1 - l2) <= 3 for l1, l2 in pairwise(levels)
            )

            if is_safe:
                safe_reports += 1

    print(safe_reports)


if __name__ == "__main__":
    main()
