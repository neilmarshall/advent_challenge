"""Solution to Problem 6, 2024"""

# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from enum import IntEnum

class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

def is_loop(original_grid : list[list[str]], candidate : tuple[int, int]) -> bool:
    grid = [row[:] for row in original_grid]
    grid[candidate[0]][candidate[1]] = '#'
    r = c = 0
    height, width = len(grid), len(grid[0])
    visited = set()
    while grid[r][c] != '^':
        if c == width - 1:
            r += 1
            c = 0
        else:
            c += 1
        if r == height - 1 and c == width - 1:
            return False
    direction = Direction.NORTH
    while True:
        # termination conditions
        if (r, c, direction) in visited:
            return True
        if r == 0 or r == height - 1 or c == 0 or c == width - 1:
            return False

        # mark that we have visited this location
        visited.add((r, c, direction))

        # establish next location to visit, and re-orient if we have hit an obstruction
        r0, c0 = r, c
        if direction == Direction.NORTH:
            r -= 1
        if direction == Direction.EAST:
            c += 1
        if direction == Direction.SOUTH:
            r += 1
        if direction == Direction.WEST:
            c -= 1
        if grid[r][c] == '#':
            r, c = r0, c0
            direction = (direction + 1) % 4

def count_loops(grid : list[list[str]]) -> int:
    return sum(1 for r in range(len(grid)) for c in range(len(grid[0])) if is_loop(grid, (r, c)))

def count_positions(grid : list[list[str]]) -> int:
    r = c = 0
    height, width = len(grid), len(grid[0])
    visited = set()
    while grid[r][c] != '^':
        if c == width - 1:
            r += 1
            c = 0
        else:
            c += 1
    direction = Direction.NORTH
    while True:
        # mark that we have visited this location
        visited.add((r, c))

        # termination condition
        if r == 0 or r == height - 1 or c == 0 or c == width - 1:
            return len(visited)

        # establish next location to visit, and re-orient if we have hit an obstruction
        r0, c0 = r, c
        if direction == Direction.NORTH:
            r -= 1
        if direction == Direction.EAST:
            c += 1
        if direction == Direction.SOUTH:
            r += 1
        if direction == Direction.WEST:
            c -= 1
        if grid[r][c] == '#':
            r, c = r0, c0
            direction = (direction + 1) % 4

if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        data = [list(line.strip()) for line in f.readlines()]

    # compute solution to part A - should be 5461
    print(count_positions(data))

    # compute solution to part B - should be 1836
    print(count_loops(data))
