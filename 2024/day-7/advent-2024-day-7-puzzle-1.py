"""
Day 7: Bridge Repair --- Part One
https://adventofcode.com/2024/day/7
"""

import operator
import itertools


def main():
    with open("input") as f:
        equations = f.read().splitlines()

    calibration_total = 0

    for equation in equations:
        expected, values = equation.split(": ")
        expected = int(expected)
        values = tuple(int(v) for v in values.split(" "))

        for ops in itertools.product([operator.add, operator.mul], repeat=len(values)):
            values_iter = iter(values)
            result = next(values_iter)

            for value, op in zip(values_iter, ops):
                result = op(result, value)

            if result == expected:
                calibration_total += result
                break

    print(calibration_total)


if __name__ == "__main__":
    main()
