"""
Day 11: Plutonian Pebbles --- Part Two
https://adventofcode.com/2024/day/11
"""

import functools


@functools.cache
def blink(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        half_len = len(stone_str) // 2
        return [int(stone_str[:half_len]), int(stone_str[half_len:])]
    else:
        return [stone * 2024]


def blink_all(stones):
    blinked = []

    for stone in stones:
        blinked.extend(blink(stone))

    return blinked


def count_stones(stones, blinks, blink_map):
    if blinks == 25:
        return sum(len(blink_map[s]) for s in stones)

    count = 0

    for stone in stones:
        count += count_stones(blink_map[stone], blinks - 25, blink_map)

    return count


def main():
    with open("input") as f:
        stones = tuple(int(s) for s in f.read().strip().split(" "))

    blink_map = {}

    for _ in range(5):
        if not blink_map:
            blink_stones = stones
        else:
            blink_stones = list(set(s for l in blink_map.values() for s in l if s not in blink_map))

        for blink_stone in blink_stones:
            blinking = [blink_stone]
            
            for _ in range(25):
                blinking = blink_all(blinking)

            blink_map[blink_stone] = blinking

    print("Finished building blink_map")

    count = count_stones(stones, 75, blink_map)

    print(count)


if __name__ == "__main__":
    main()
