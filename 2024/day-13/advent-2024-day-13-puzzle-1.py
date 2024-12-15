"""
Day 13: Claw Contraption --- Part One
https://adventofcode.com/2024/day/13
"""

import re
from dataclasses import dataclass


@dataclass
class Machine:
    a_x: int
    a_y: int
    b_x: int
    b_y: int
    prize_x: int
    prize_y: int


def main():
    machines = []

    with open("input") as f:
        for line in f:
            if m := re.match(r"Button A: X\+(\d+), Y\+(\d+)", line):
                a_x = int(m.group(1))
                a_y = int(m.group(2))
            elif m := re.match(r"Button B: X\+(\d+), Y\+(\d+)", line):
                b_x = int(m.group(1))
                b_y = int(m.group(2))
            elif m := re.match(r"Prize: X=(\d+), Y=(\d+)", line):
                prize_x = int(m.group(1))
                prize_y = int(m.group(2))
                machine = Machine(a_x, a_y, b_x, b_y, prize_x, prize_y)
                machines.append(machine)

    max_presses = 100
    a_cost = 3
    b_cost = 1

    prizes = 0
    minimum_cost = 0

    for machine in machines:
        costs = []

        for a_presses in range(max_presses + 1):
            x = a_presses * machine.a_x
            y = a_presses * machine.a_y

            if x > machine.prize_x or y > machine.prize_y:
                continue

            remaining_x = machine.prize_x - x
            remaining_y = machine.prize_y - y

            if remaining_x % machine.b_x or remaining_y % machine.b_y:
                continue

            b_presses_x = remaining_x // machine.b_x
            b_presses_y = remaining_y // machine.b_y

            if b_presses_x != b_presses_y:
                continue

            cost = a_presses * a_cost + b_presses_x * b_cost
            costs.append(cost)

        prizes += 1
        minimum_cost += min(costs, default=0)

    print(minimum_cost)


if __name__ == "__main__":
    main()
