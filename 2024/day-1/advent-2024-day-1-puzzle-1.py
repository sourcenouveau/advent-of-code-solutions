"""
Day 1: Historian Hysteria --- Part One
https://adventofcode.com/2024/day/1
"""


def main():
    with open("input") as f:
        left, right = zip(*(map(int, line.strip().split("   ")) for line in f))

    distance = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))

    print(distance)


if __name__ == "__main__":
    main()
