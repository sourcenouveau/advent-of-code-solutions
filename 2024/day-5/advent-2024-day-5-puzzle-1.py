"""
Day 5: Print Queue --- Part One
https://adventofcode.com/2024/day/5
"""


def main():
    with open("input") as f:
        ordering = {}

        for line in f:
            line = line.strip()

            if not line:
                break

            before, after = map(int, line.split("|"))

            if before not in ordering:
                ordering[before] = set()

            ordering[before].add(after)

        middle_sum = 0

        for line in f:
            line = line.strip()

            update = list(map(int, line.split(",")))
            wrong_order = False

            for i in range(len(update)):
                for j in range(len(update)):
                    current = update[i]

                    if j < i:
                        before = update[j]

                        if before in ordering.get(current, set()):
                            wrong_order = True
                            break
                    elif j > i:
                        after = update[j]

                        if current in ordering.get(after, set()):
                            wrong_order = True
                            break
                    else:
                        continue

                if wrong_order:
                    break

            if not wrong_order:
                middle_sum += update[len(update) // 2]

    print(middle_sum)


if __name__ == "__main__":
    main()
