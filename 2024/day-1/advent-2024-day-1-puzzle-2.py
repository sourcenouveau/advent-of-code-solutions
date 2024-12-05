"""
Day 1: Historian Hysteria --- Part Two
https://adventofcode.com/2024/day/1
"""


def main():
    with open("input") as f:
        left, right = zip(*(map(int, line.strip().split("   ")) for line in f))

    counts = {}

    for r in right:
        counts[r] = counts.get(r, 0) + 1

    similarity = 0

    for l in left:
        similarity += l * counts.get(l, 0)

    print(similarity)


if __name__ == "__main__":
    main()
