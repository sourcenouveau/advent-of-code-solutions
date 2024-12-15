"""
Day 14: Restroom Redoubt --- Part One
https://adventofcode.com/2024/day/14
"""

import math
import re


def main():
    w = 101
    h = 103

    robots = []

    with open("input") as f:
        for line in f:
            px, py, vx, vy = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line).groups()
            robots.append([int(px), int(py), int(vx), int(vy)])

    for _ in range(100):
        for r in robots:
            r[0] = (r[0] + r[2]) % w
            r[1] = (r[1] + r[3]) % h

    q = [0] * 4
    half_w = w // 2
    half_h = h // 2

    for r in robots:
        left = r[0] < half_w
        right = r[0] > half_w
        up = r[1] < half_h
        down = r[1] > half_h

        if left and up:
            q[0] += 1
        elif right and up:
            q[1] += 1
        elif left and down:
            q[2] += 1
        elif right and down:
            q[3] += 1

    safety_factor = math.prod(q)

    print(safety_factor)


if __name__ == "__main__":
    main()
