# Advent of Code 2019 Solutions: Day 2, Puzzle 2
# https://github.com/emddudley/advent-of-code-solutions


with open("input", "r") as f:
    memory = [int(x) for x in f.read().strip().split(",")]

done = False

for noun in range(0, 100):
    for verb in range(0, 100):
        program = memory.copy()
        program[1] = noun
        program[2] = verb

        for opcode_index in range(0, len(program), 4):
            opcode = program[opcode_index]

            if opcode == 99:
                break

            addr_a = program[opcode_index + 1]
            addr_b = program[opcode_index + 2]
            dest = program[opcode_index + 3]

            if opcode == 1:
                program[dest] = program[addr_a] + program[addr_b]
            elif opcode == 2:
                program[dest] = program[addr_a] * program[addr_b]

        if program[0] == 19690720:
            print(noun)
            print(verb)
            print(100 * noun + verb)
            done = True
            break

    if done:
        break
