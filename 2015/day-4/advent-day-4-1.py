# Advent of Code Solutions: Day 4, part 1
# https://github.com/emddudley/advent-of-code-solutions

import hashlib

with open('input', 'r') as input:
    secret = input.read()

answer = 1

while True:
    digest = hashlib.md5(secret + str(answer)).hexdigest()
    if digest[0:5] == '00000': break
    answer += 1

print(answer)
