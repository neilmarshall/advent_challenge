"""Solution to Problem 4, 2024"""

import unittest

class TestCountXmas(unittest.TestCase):
    grid = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]

    def test_count_xmas_part_a(self):
        self.assertEqual(count_xmas_part_a(self.grid), 18)

    def test_count_xmas_part_b(self):
        self.assertEqual(count_xmas_part_b(self.grid), 9)

def count_xmas_part_a(grid : list[list[str]]) -> int:
    def horizontal_matches(r : int, c : int) -> int:
        matches = 0
        try:
            if grid[r][c] == 'X' and grid[r][c + 1] == 'M' and grid[r][c + 2] == 'A' and grid[r][c + 3] == 'S':
                matches += 1
        except IndexError:
            pass
        try:
            if c - 3 < 0:
                raise IndexError()
            if grid[r][c] == 'X' and grid[r][c - 1] == 'M' and grid[r][c - 2] == 'A' and grid[r][c - 3] == 'S':
                matches += 1
        except IndexError:
            pass
        return matches
    def vertical_matches(r : int, c : int) -> int:
        matches = 0
        try:
            if grid[r][c] == 'X' and grid[r + 1][c] == 'M' and grid[r + 2][c] == 'A' and grid[r + 3][c] == 'S':
                matches += 1
        except IndexError:
            pass
        try:
            if r - 3 < 0:
                raise IndexError()
            if grid[r][c] == 'X' and grid[r - 1][c] == 'M' and grid[r - 2][c] == 'A' and grid[r - 3][c] == 'S':
                matches += 1
        except IndexError:
            pass
        return matches
    def diagonal_matches(r : int, c : int) -> int:
        matches = 0
        try:
            if grid[r][c] == 'X' and grid[r + 1][c + 1] == 'M' and grid[r + 2][c + 2] == 'A' and grid[r + 3][c + 3] == 'S':
                matches += 1
        except IndexError:
            pass
        try:
            if r - 3 < 0 or c - 3 < 0:
                raise IndexError()
            if grid[r][c] == 'X' and grid[r - 1][c - 1] == 'M' and grid[r - 2][c - 2] == 'A' and grid[r - 3][c - 3] == 'S':
                matches += 1
        except IndexError:
            pass
        try:
            if c - 3 < 0:
                raise IndexError()
            if grid[r][c] == 'X' and grid[r + 1][c - 1] == 'M' and grid[r + 2][c - 2] == 'A' and grid[r + 3][c - 3] == 'S':
                matches += 1
        except IndexError:
            pass
        try:
            if r - 3 < 0:
                raise IndexError()
            if grid[r][c] == 'X' and grid[r - 1][c + 1] == 'M' and grid[r - 2][c + 2] == 'A' and grid[r - 3][c + 3] == 'S':
                matches += 1
        except IndexError:
            pass
        return matches
    xmas_count = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            xmas_count += horizontal_matches(r, c)
            xmas_count += vertical_matches(r, c)
            xmas_count += diagonal_matches(r, c)
    return xmas_count

def count_xmas_part_b(grid : list[list[str]]) -> int:
    def is_match(r : int, c : int) -> bool:
        if r + 2 < len(grid) and c + 2 < len(grid[0]):
            if grid[r + 1][c + 1] != 'A':
                return False
            if (grid[r][c] == 'M' and grid[r + 2][c + 2] == 'S') or (grid[r][c] == 'S' and grid[r + 2][c + 2] == 'M'):
                return (grid[r][c + 2] == 'M' and grid[r + 2][c] == 'S') or (grid[r][c + 2] == 'S' and grid[r + 2][c] == 'M')
        return False
    return sum(1 for r in range(len(grid)) for c in range(len(grid[r])) if is_match(r, c))

if __name__ == "__main__":
    unittest.main(exit=False)

    with open("input.txt", encoding="utf-8") as f:
        GRID = [list(row) for row in f.readlines()]

    # compute solution to part A - should be 2414
    print(count_xmas_part_a(GRID))

    # compute solution to part B - should be 1871
    print(count_xmas_part_b(GRID))
