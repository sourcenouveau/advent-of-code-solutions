"""
Day 13: Claw Contraption --- Part Two
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

    def solve(self):
        a_presses = (self.b_y * self.prize_x - self.b_x * self.prize_y) // (
            self.b_y * self.a_x - self.b_x * self.a_y
        )
        b_presses = (self.prize_y - (self.a_y * a_presses)) // self.b_y

        if (
            a_presses * self.a_x + b_presses * self.b_x != self.prize_x
            or a_presses * self.a_y + b_presses * self.b_y != self.prize_y
        ):
            return None, None

        return a_presses, b_presses


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
                prize_x = int(m.group(1)) + 10000000000000
                prize_y = int(m.group(2)) + 10000000000000
                machine = Machine(a_x, a_y, b_x, b_y, prize_x, prize_y)
                machines.append(machine)

    a_cost = 3
    b_cost = 1

    minimum_cost = 0

    for machine in machines:
        a_presses, b_presses = machine.solve()

        if a_presses is None:
            continue

        minimum_cost += a_presses * a_cost + b_presses * b_cost

    print(minimum_cost)


if __name__ == "__main__":
    main()
