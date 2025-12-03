"""
Day 1: Secret Entrance --- Part Two
https://adventofcode.com/2025/day/1
"""


def main():
    dial_position = 50
    zero_count = 0

    with open("input") as f:
        for line in f:
            turn_direction = line[0]
            clicks = int(line[1:])

            full_rotations = clicks // 100
            partial_rotation = (clicks % 100) != 0
            zero_count += full_rotations

            if turn_direction == "L":
                clicks = -clicks

            next_position = (dial_position + clicks) % 100

            if (
                partial_rotation
                and dial_position != 0
                and (
                    (clicks > 0 and next_position < dial_position)
                    or (clicks < 0 and next_position > dial_position)
                    or next_position == 0
                )
            ):
                zero_count += 1

            dial_position = next_position

    print(zero_count)


if __name__ == "__main__":
    main()
