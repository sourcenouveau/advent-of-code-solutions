# Advent of Code Solutions: Day 5, part 1
# https://github.com/emddudley/advent-of-code-solutions

def count_letters(string, letters):
    count = 0
    for letter in letters:
        count += string.count(letter)
    return count

def is_nice(naughty_or_nice):
    vowel_count = count_letters(naughty_or_nice, 'aeiou')

    if vowel_count < 3: return False

    repeated_letter = False

    for i in range(0, len(naughty_or_nice) - 2):
        if naughty_or_nice[i] == naughty_or_nice[i + 1]:
            repeated_letter = True
            break

    if not repeated_letter: return False

    if ('ab' in naughty_or_nice
        or 'cd'  in naughty_or_nice
        or 'pq' in naughty_or_nice
        or 'xy' in naughty_or_nice): return False

    return True

nice_count = 0

with open('input', 'r') as input:
    for line in input:
        if is_nice(line):
            nice_count += 1

print(nice_count)
