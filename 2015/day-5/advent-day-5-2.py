# Advent of Code Solutions: Day 5, part 2
# https://github.com/emddudley/advent-of-code-solutions


def is_nice(naughty_or_nice):
    repeating_pair = False

    for i in range(0, len(naughty_or_nice) - 2):
        first_pair = naughty_or_nice[i : (i + 2)]

        for j in range(i + 2, len(naughty_or_nice) - 2):
            second_pair = naughty_or_nice[j : (j + 2)]

            if second_pair == first_pair:
                repeating_pair = True
                break

        if repeating_pair:
            break

    if not repeating_pair:
        return False

    letter_sandwich = False

    for i in range(0, len(naughty_or_nice) - 3):
        if naughty_or_nice[i] == naughty_or_nice[i + 2]:
            letter_sandwich = True
            break

    if not letter_sandwich:
        return False

    return True


nice_count = 0

with open("input", "r") as input:
    for line in input:
        if is_nice(line):
            nice_count += 1

print(nice_count)
