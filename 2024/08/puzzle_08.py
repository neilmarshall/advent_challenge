"""Solution to Problem 8, 2024"""

# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name

import unittest
from itertools import product

class EquationIsValidFixture(unittest.TestCase):
    def test_count_antinodes(self):
        test_data = [
            "............",
            "........0...",
            ".....0......",
            ".......0....",
            "....0.......",
            "......A.....",
            "............",
            "............",
            "........A...",
            ".........A..",
            "............",
            "............"
        ]
        grid = [list(row) for row in test_data]
        self.assertEqual(count_antinodes(grid), 14)
        self.assertEqual(count_antinodes(grid, extend=True), 34)

    def test_count_antinodes_with_expansion(self):
        test_data = [
            "T.........",
            "...T......",
            ".T........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]
        grid = [list(row) for row in test_data]
        self.assertEqual(count_antinodes(grid, extend=True), 9)

def count_antinodes(grid : list[list[str]], extend : bool = False) -> int:
    # compute antenna locations
    antenna_locations = {}
    # pylint: disable=consider-using-enumerate
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != '.':
                if grid[r][c] not in antenna_locations:
                    antenna_locations[grid[r][c]] = []
                antenna_locations[grid[r][c]].append((r, c))

    # compute antinode locations
    antinodes = set()
    if extend:
        for locations in antenna_locations.values():
            for antenna in locations:
                antinodes.add(antenna)
    for value in antenna_locations.values():
        for a, b in product(value, value):
            if a != b:
                delta = (b[0] - a[0], b[1] - a[1])

                # add to b
                new_node = b
                while True:
                    new_node = new_node[0] + delta[0], new_node[1] + delta[1]
                    if 0 <= new_node[0] < len(grid) and 0 <= new_node[1] < len(grid[0]):
                        antinodes.add(new_node)
                    else:
                        break
                    if not extend:
                        break

                # subtract from a
                new_node = a
                while True:
                    new_node = new_node[0] - delta[0], new_node[1] - delta[1]
                    if 0 <= new_node[0] < len(grid) and 0 <= new_node[1] < len(grid[0]):
                        antinodes.add(new_node)
                    else:
                        break
                    if not extend:
                        break
    return len(antinodes)

if __name__ == "__main__":
    unittest.main(exit=False)

    with open("input.txt", encoding="utf-8") as f:
        grid = [list(row.strip()) for row in f.readlines()]

    # compute solution to part A - should be 396
    print(count_antinodes(grid))

    # compute solution to part B - should be 1200
    print(count_antinodes(grid, extend=True))
