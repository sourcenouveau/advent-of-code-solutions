"""
Day 4: Scratchcards --- Part One
https://adventofcode.com/2023/day/4
"""


def main():
    cards = []

    with open("input") as f:
        for line in f:
            winning, have = line.strip().split(":")[1].split("|")
            cards.append((
                tuple(int(w) for w in winning.split(" ") if w),
                tuple(int(h) for h in have.split(" ") if h)
            ))

    total_points = 0

    for winning, have in cards:
        points = 0

        for h in have:
            if h in winning:
                if points:
                    points *= 2
                else:
                    points = 1

        total_points += points

    print(total_points)


if __name__ == "__main__":
    main()
