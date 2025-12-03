"""
Day 1: Secret Entrance --- Part One
https://adventofcode.com/2025/day/1
"""


def main():
    dial_position = 50
    zero_count = 0

    with open("input") as f:
        for line in f:
            turn_direction = line[0]
            clicks = int(line[1:])

            if turn_direction == "L":
                clicks = -clicks

            dial_position = (dial_position + clicks) % 100

            if dial_position == 0:
                zero_count += 1

    print(zero_count)


if __name__ == "__main__":
    main()
