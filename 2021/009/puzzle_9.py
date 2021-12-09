from functools import reduce
from operator import mul

def identify_low_points(points):
    low_points = []
    for r in range(len(points)):
        for c in range(len(points[r])):
            if r != 0:
                if points[r][c] >= points[r - 1][c]:
                    continue
            if r != len(points) - 1:
                if points[r][c] >= points[r + 1][c]:
                    continue
            if c != 0:
                if points[r][c] >= points[r][c - 1]:
                    continue
            if c != len(points[r]) - 1:
                if points[r][c] >= points[r][c + 1]:
                    continue
            low_points.append((r, c))
    return low_points


def value_low_Points(points):
    """
    >>> points = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0], [3, 9, 8, 7, 8, 9, 4, 9, 2, 1], [9, 8, 5, 6, 7, 8, 9, 8, 9, 2], [8, 7, 6, 7, 8, 9, 6, 7, 8, 9], [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]
    >>> value_low_Points(points)
    15
    """
    low_points = [points[r][c] for r, c in identify_low_points(points)]
    return sum(low_points) + len(low_points)


def value_basins(points):
    """
    >>> points = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0], [3, 9, 8, 7, 8, 9, 4, 9, 2, 1], [9, 8, 5, 6, 7, 8, 9, 8, 9, 2], [8, 7, 6, 7, 8, 9, 6, 7, 8, 9], [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]
    >>> value_basins(points)
    1134
    """
    def get_basin(r, c):
        basin, checked_neighbours, unchecked_neighbours = set(), set(), set(((r, c),))
        def add_neighbours(r, c):
            basin.add((r, c))
            checked_neighbours.add((r, c))
            if r > 0:
                if points[r - 1][c] != 9:
                    basin.add((r - 1, c))
                    if (r - 1, c) not in checked_neighbours:
                        unchecked_neighbours.add((r - 1, c))
            if r < len(points) - 1:
                if points[r + 1][c] != 9:
                    basin.add((r + 1, c))
                    if (r + 1, c) not in checked_neighbours:
                        unchecked_neighbours.add((r + 1, c))
            if c > 0:
                if points[r][c - 1] != 9:
                    basin.add((r, c - 1))
                    if (r, c - 1) not in checked_neighbours:
                        unchecked_neighbours.add((r, c - 1))
            if c < len(points[r]) - 1:
                if points[r][c + 1] != 9:
                    basin.add((r, c + 1))
                    if (r, c + 1) not in checked_neighbours:
                        unchecked_neighbours.add((r, c + 1))
        while unchecked_neighbours:
            add_neighbours(*unchecked_neighbours.pop())
        return basin
    basins = (get_basin(r, c) for r, c in identify_low_points(points))
    return reduce(mul, map(len, sorted(basins, key=len, reverse=True)[:3]), 1)


if __name__ == "__main__":
    import doctest; doctest.testmod()
    with open("input.txt") as f:
        points = [[*map(int, r.strip())] for r in f]
    print(f"Solution to Puzzle 9, Part A: {value_low_Points(points)}")  # should equal 439
    print(f"Solution to Puzzle 9, Part B: {value_basins(points)}")  # should equal 900900