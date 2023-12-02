"""
Day 1: Trebuchet?!
https://adventofcode.com/2023/day/1
"""

def main():
    cal_sum = 0

    with open("input") as f:
        for line in f:
            first = None
            second = None

            for c in line:
                try:
                    cal_val = int(c)

                    if first is None:
                        first = cal_val

                    second = cal_val
                except ValueError:
                    continue

            cal_sum += 10 * first + second

    print(cal_sum)


if __name__ == "__main__":
    main()
