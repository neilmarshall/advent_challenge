"""Advent of Code 2025 - Puzzle 6 - https://adventofcode.com/2025/day/6"""
# pylint: disable=missing-function-docstring

import re
from functools import reduce

inputs, words, operands = [], [], []
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if re.search(r'\d+', line) is not None:
            inputs.append([int(c) for c in line.split()])
        else:
            operands = line.split()
        for i, word in enumerate(line):
            if len(words) < i + 1:
                words.append([])
            if re.match('\d', word) is not None:
                words[i] += word

# part A
total : int = 0
for i, operand in enumerate(operands):
    if operand == '+':
        total += reduce(lambda t, s: t + s, (input[i] for input in inputs), 0)
    elif operand == '*':
        total += reduce(lambda t, s: t * s, (input[i] for input in inputs), 1)
    else:
        raise NotImplementedError(f'Unrecognized operand: {operand}')
print(f"Solution to Part A: {total}")  # solution to part A: 4771265398012

# part B
total : int = 0
counter : int = 0
numbers = []
for word in words:
    if len(word) > 0:
        numbers.append(int(str.join('', word)))
    else:
        operand = operands[counter]
        if operand == '+':
            total += reduce(lambda t, s: t + s, numbers, 0)
        elif operand == '*':
            total += reduce(lambda t, s: t * s, numbers, 1)
        else:
            raise NotImplementedError(f'Unrecognized operand: {operand}')
        numbers = []
        counter += 1
print(f"Solution to Part B: {total}")  # solution to part B: 10695785245101
