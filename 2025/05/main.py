"""Advent of Code 2025 - Puzzle 5 - https://adventofcode.com/2025/day/5"""
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring

import re

def try_reduce_ranges(ranges):
    for rng1, rng2 in zip(ranges, ranges[1:]):
        if rng2[0] <= rng1[1]:
            new_rng = (rng1[0], max(rng1[1], rng2[1]))
            idx = ranges.index(rng1)
            ranges[idx] = new_rng
            del ranges[idx + 1]
            return True
    return False

def main():
    ranges, ingredients = [], []
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            range_match = re.match(r'^(\d+)\-(\d+)$', line.strip())
            ingredient_match = re.match(r'^\d+$', line.strip())
            if range_match is not None:
                start, end = int(range_match.group(1)), int(range_match.group(2))
                ranges.append((start, end))
            elif ingredient_match is not None:
                ingredients.append(int(ingredient_match.string))

    ranges.sort()
    while try_reduce_ranges(ranges):
        pass

    # part A
    def is_fresh(ingredient):
        return any(start <= ingredient <= end for start, end in ranges)
    print(f"Solution to Part A: {len(list(filter(is_fresh, ingredients)))}")  # solution to part A: 789

    # part B
    print(f"Solution to Part B: {sum(b - a + 1 for a, b in ranges)}")  # solution to part B: 343329651880509

if __name__ == "__main__":
    main()
