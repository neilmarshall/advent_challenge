from itertools import chain
from math import copysign

def count_overlapping_lines(points, include_diagonals=False):
    """
    >>> points = [((0, 9), (5, 9)), ((8, 0), (0, 8)), ((9, 4), (3, 4)), ((2, 2), (2, 1)), ((7, 0), (7, 4)), ((6, 4), (2, 0)), ((0, 9), (2, 9)), ((3, 4), (1, 4)), ((0, 0), (8, 8)), ((5, 5), (8, 2))]
    >>> count_overlapping_lines(points)
    5

    >>> count_overlapping_lines(points, True)
    12
    """
    width = max(p[0] for p in chain.from_iterable(points)) + 1
    height = max(p[1] for p in chain.from_iterable(points)) + 1
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for ((x0, y0), (x1, y1)) in points:
        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                grid[y][x0] += 1
        elif y0 == y1:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                grid[y0][x] += 1
        elif include_diagonals:
            y, step = y0, int(copysign(1, y1 - y0))
            rng = range(x0, x1 + 1) if x0 < x1 else range(x0, x1 - 1, -1)
            for x in rng:
                grid[y][x] += 1
                y += step
    return sum(sum(1 for c in r if c >= 2) for r in grid)


if __name__ == "__main__":
    import doctest; doctest.testmod()
    def parse_row(row):
        p0, p1 = row.split(" -> ")
        return (tuple(map(int, p0.split(","))), tuple(map(int, p1.split(","))))
    with open("input.txt") as f:
        points = list(map(parse_row, f))
    print(f"Solution to Puzzle 5, Part A: {count_overlapping_lines(points)}")  # should equal 5306
    print(f"Solution to Puzzle 5, Part B: {count_overlapping_lines(points, True)}")  # should equal 17787
