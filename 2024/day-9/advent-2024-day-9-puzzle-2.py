"""
Day 9: Disk Fragmenter --- Part Two
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

    file_end = len(disk) - 1

    while file_end >= 0:
        while file_end >= 0 and disk[file_end] == -1:
            file_end -= 1

        file_start = file_end

        while file_start >= 0:
            if disk[file_start - 1] != disk[file_end]:
                break

            file_start -= 1

        file_length = file_end - file_start + 1

        gap_start = 0

        while gap_start < file_start:
            while gap_start < file_start:
                if disk[gap_start] == -1:
                    break

                gap_start += 1
            else:
                continue

            gap_end = gap_start

            while gap_end < file_start:
                if disk[gap_end + 1] != -1:
                    break

                gap_end += 1

            gap_length = gap_end - gap_start + 1

            if gap_length >= file_length:
                break

            gap_start = gap_end + 1
        else:
            file_end = file_start - 1
            continue

        for i in range(file_length):
            disk[gap_start + i] = disk[file_start + i]
            disk[file_start + i] = -1

        file_end = file_start - 1

    checksum = 0

    for block, file_id in enumerate(disk):
        if file_id == -1:
            continue

        checksum += block * file_id

    print(checksum)


if __name__ == "__main__":
    main()
