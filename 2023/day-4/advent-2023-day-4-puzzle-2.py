"""
Day 4: Scratchcards --- Part Two
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

    copy_counts = [1] * len(cards)

    for c, (winning, have) in enumerate(cards):
        won = sum(1 for h in have if h in winning)

        for w in range(c + 1, c + 1 + won):
            copy_counts[w] += copy_counts[c]

    print(sum(copy_counts))


if __name__ == "__main__":
    main()
