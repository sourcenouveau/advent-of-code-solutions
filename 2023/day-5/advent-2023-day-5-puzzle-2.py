"""
Day 5: If You Give A Seed A Fertilizer --- Part Two
https://adventofcode.com/2023/day/5
"""


def lookup(src_val, dst_map):
    dst_val = src_val

    for dst_start, src_start, src_len in dst_map:
        if src_start <= src_val < src_start + src_len:
             dst_val = dst_start + (src_val - src_start)

    return dst_val


def main():
    maps = {}  # {map_to: tuple(dst_start, src_start, src_len)}
    next_maps = {}
    seed_ranges = []

    with open("input") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith("seeds: "):
                seed_items = tuple(int(s) for s in line[len("seeds: "):].split(" "))

                for seed_start, seed_len in zip(*[iter(seed_items)] * 2):
                    seed_ranges.append((seed_start, seed_len))

                continue

            if line.endswith(" map:"):
                map_from, map_to = line[:-len(" map:")].split("-to-")
                maps[map_to] = []
                next_maps[map_from] = map_to
                continue

            maps[map_to].append(tuple(int(i) for i in line.split(" ")))

    lowest_loc = None

    for seed_start, seed_len in seed_ranges:
        for seed in range(seed_start, seed_start + seed_len):
            src_val = seed
            dst_map = "soil"

            while dst_map:
                src_val = lookup(src_val, maps[dst_map])
                dst_map = next_maps.get(dst_map)

            if lowest_loc is None or src_val < lowest_loc:
                lowest_loc = src_val

    print(lowest_loc)


if __name__ == "__main__":
    main()
