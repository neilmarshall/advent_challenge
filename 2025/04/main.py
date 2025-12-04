"""Advent of Code 2025 - Puzzle 4 - https://adventofcode.com/2025/day/4"""
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring

def count_adjacent_rolls(grid, r, c):
    total = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == 0 and j == 0:
                continue
            if r + i >= 0 and r + i < len(grid):
                if c + j >= 0 and c + j < len(grid[r]):
                    if grid[r + i][c + j] == '@':
                        total += 1
    return total

def get_accessible_rolls(grid):
    for r, _ in enumerate(grid):
        for c, _ in enumerate(grid[r]):
            if grid[r][c] == '@' and count_adjacent_rolls(grid, r, c) < 4:
                yield r, c

def remove_accessible_rolls(grid, accessible_rolls):
    for r, c in accessible_rolls:
        s = list(grid[r])
        s[c] = '.'
        grid[r] = str.join('', s)

def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        grid = [row.strip() for row in f.readlines()]

    # part A
    print(f"Solution to Part A: {len(list(get_accessible_rolls(grid)))}")  # solution to part A: 1,478

    # part B
    accessible_roll_count : int = 0
    while True:
        accessible_rolls = list(get_accessible_rolls(grid))
        if len(accessible_rolls) == 0:
            break
        accessible_roll_count += len(accessible_rolls)
        remove_accessible_rolls(grid, accessible_rolls)
    print(f"Solution to Part B: {accessible_roll_count}")  # solution to part B: 9,120

if __name__ == "__main__":
    main()
