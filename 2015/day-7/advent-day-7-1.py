# Advent of Code Solutions: Day 7, part 1
# https://github.com/emddudley/advent-of-code-solutions

from collections import namedtuple

Connection = namedtuple("Connection", "l op r")


def add_connection(connection, circuit):
    tokens = connection.strip().split(" ")
    l = tokens[len(tokens) - 5] if len(tokens) > 4 else None
    op = tokens[len(tokens) - 4] if len(tokens) > 3 else None
    r = tokens[len(tokens) - 3]
    wire = tokens[len(tokens) - 1]
    circuit[wire] = Connection(l, op, r)


def eval_wire(wire, circuit, signals=None):
    if signals == None:
        signals = {}
    if wire.isdigit():
        return int(wire)
    if wire in signals:
        return signals[wire]

    if circuit[wire].op == None:
        signals[wire] = eval_wire(circuit[wire].r, circuit, signals)
    elif circuit[wire].op == "NOT":
        signals[wire] = ~eval_wire(circuit[wire].r, circuit, signals)
    elif circuit[wire].op == "AND":
        signals[wire] = eval_wire(circuit[wire].l, circuit, signals) & eval_wire(
            circuit[wire].r, circuit, signals
        )
    elif circuit[wire].op == "OR":
        signals[wire] = eval_wire(circuit[wire].l, circuit, signals) | eval_wire(
            circuit[wire].r, circuit, signals
        )
    elif circuit[wire].op == "LSHIFT":
        signals[wire] = eval_wire(circuit[wire].l, circuit, signals) << eval_wire(
            circuit[wire].r, circuit, signals
        )
    elif circuit[wire].op == "RSHIFT":
        signals[wire] = eval_wire(circuit[wire].l, circuit, signals) >> eval_wire(
            circuit[wire].r, circuit, signals
        )

    return signals[wire]


circuit = {}

with open("input", "r") as input:
    for connection in input:
        add_connection(connection, circuit)

print(eval_wire("a", circuit))
