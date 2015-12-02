# Advent of Code Solutions: Day 2, part 1
# https://github.com/emddudley/advent-of-code-solutions

with open('input', 'r') as input:
    dimensions_list = input.read().splitlines()

total_area = 0

for dimensions in dimensions_list:
    length, width, height = map(int, dimensions.split('x'))
    top = length * width
    front = width * height
    side = height * length
    smallest = min([top, front, side])
    area = 2 * top + 2 * front + 2 * side + smallest
    total_area += area

print(total_area)
