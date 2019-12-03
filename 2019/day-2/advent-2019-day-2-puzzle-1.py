# Advent of Code 2019 Solutions: Day 2, Puzzle 1
# https://github.com/emddudley/advent-of-code-solutions


with open('input', 'r') as f:
    program = [int(x) for x in f.read().strip().split(',')]

program[1] = 12
program[2] = 2

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

print(program[0])
