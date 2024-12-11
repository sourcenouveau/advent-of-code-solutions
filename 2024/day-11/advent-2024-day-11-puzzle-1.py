"""
Day 11: Plutonian Pebbles --- Part One
https://adventofcode.com/2024/day/11
"""


def main():
    with open("input") as f:
        stones = tuple(int(s) for s in f.read().strip().split(" "))

    for _ in range(25):
        after = []

        for stone in stones:
            if stone == 0:
                after.append(1)
            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                half_len = len(stone_str) // 2
                after.append(int(stone_str[:half_len]))
                after.append(int(stone_str[half_len:]))
            else:
                after.append(stone * 2024)

        stones = after

    print(len(stones))


if __name__ == "__main__":
    main()
