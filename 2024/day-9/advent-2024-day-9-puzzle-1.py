"""
Day 9: Disk Fragmenter --- Part One
https://adventofcode.com/2024/day/9
"""


def main():
    with open("input") as f:
        disk_map = f.read().strip()

    disk = []
    is_file = True
    file_id = 0

    for d in disk_map:
        label = file_id if is_file else -1

        for _ in range(int(d)):
            disk.append(label)

        file_id = file_id + 1 if is_file else file_id
        is_file = not is_file

    move_to = 0
    move_from = len(disk) - 1

    while True:
        while move_to < len(disk) and disk[move_to] != -1:
            move_to += 1

        while move_from >= 0 and disk[move_from] == -1:
            move_from -= 1

        if move_from <= move_to:
            break

        disk[move_to] = disk[move_from]
        disk[move_from] = -1

    checksum = 0

    for block, file_id in enumerate(disk):
        if file_id == -1:
            continue

        checksum += block * file_id

    print(checksum)


if __name__ == "__main__":
    main()
