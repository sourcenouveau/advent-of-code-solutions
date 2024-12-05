"""
Day 2: Red-Nosed Reports --- Part Two
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
            bad_level = None
            is_safe = True
            i = 0

            while i < len(levels) - 1:
                l1 = levels[i]
                l2 = levels[i + 1]
                not_monotonic = not compare(l1, l2)
                large_step = abs(l1 - l2) > 3

                if not_monotonic or large_step:
                    if bad_level is None:
                        bad_level = i
                        del levels[i]
                    else:
                        is_safe = False
                        break
                else:
                    i += 1

            if is_safe:
                safe_reports += 1

    print(safe_reports)


if __name__ == "__main__":
    main()
