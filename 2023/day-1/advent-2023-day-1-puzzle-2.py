"""
Part Two
https://adventofcode.com/2023/day/1
"""

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def main():
    cal_sum = 0

    with open("input") as f:
        for line in f:
            first = None
            second = None

            for i, c in enumerate(line):
                if c.isdigit():
                    cal_val = int(c)
                else:
                    for number in numbers:
                        if line[i:].startswith(number):
                            cal_val = numbers[number]
                            break
                    else:
                        continue

                if first is None:
                    first = cal_val

                second = cal_val

            cal_sum += 10 * first + second

    print(cal_sum)


if __name__ == "__main__":
    main()
