"""
Day 5: Print Queue --- Part Two
https://adventofcode.com/2024/day/5
"""

import functools


@functools.total_ordering
class Page:
    def __init__(self, page) -> None:
        self.page = page
        self.afters = []

    def __eq__(self, value: object) -> bool:
        return value == self.page

    def __lt__(self, value: object) -> bool:
        return value in self.afters


def main():
    with open("input") as f:
        ordering = {}

        for line in f:
            line = line.strip()

            if not line:
                break

            before, after = map(int, line.split("|"))

            if before not in ordering:
                ordering[before] = Page(before)

            ordering[before].afters.append(after)

        middle_sum = 0

        for line in f:
            update = list(ordering[p] for p in map(int, line.strip().split(",")))

            if update != sorted(update):
                middle_sum += sorted(update)[len(update) // 2].page

    print(middle_sum)


if __name__ == "__main__":
    main()
