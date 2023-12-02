"""
Day 2: Cube Conundrum --- Part Two
https://adventofcode.com/2023/day/2
"""

import operator
from functools import reduce


def main():
    power_sum = 0

    with open("input") as f:
        for line in f:
            observed = {"red": 0, "green": 0, "blue": 0}
            reveals = line.split(":")[1].split(";")

            for reveal in reveals:
                colors = [c.strip() for c in reveal.split(",")]

                for color in colors:
                    count, color_name = color.split(" ")
                    observed[color_name] = max(int(count), observed[color_name])

            power_sum += reduce(operator.mul, observed.values())

    print(power_sum)


if __name__ == "__main__":
    main()
