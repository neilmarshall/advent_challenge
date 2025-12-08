"""Advent of Code 2025 - Puzzle 7 - https://adventofcode.com/2025/day/7"""
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring

from functools import lru_cache

with open('input.txt', 'r', encoding='utf-8') as f:
    manifold = [line.strip() for line in f]

@lru_cache(maxsize=None)
def ways_to_reach(r, c):
    if r == 0:
        return c == manifold[0].index('S')
    if manifold[r - 1][c] == '^':
        return 0
    total = ways_to_reach(r - 1, c)
    if c > 0 and manifold[r - 1][c - 1] == '^':
        total += ways_to_reach(r - 1, c - 1)
    if c < len(manifold[0]) - 1 and manifold[r - 1][c + 1] == '^':
        total += ways_to_reach(r - 1, c + 1)
    return total

def main():
    # part A
    beams = set((manifold[0].index('S'),))
    splits : int = 0
    for row in manifold[1:]:
        new_beams = set(beams)
        for i, c in enumerate(row):
            if c == '^' and i in beams:
                splits += 1
                new_beams.remove(i)
                new_beams.add(i + 1)
                if i > 0:
                    new_beams.add(i - 1)
        beams = new_beams
    print(f"Solution to Part A: {splits}")  # solution to part A: 1516

    # part B
    print(f"Solution to Part B: {sum(ways_to_reach(len(manifold), c) for c in range(len(manifold[0])))}")  # solution to part B: 1393669447690

if __name__ == '__main__':
    main()
