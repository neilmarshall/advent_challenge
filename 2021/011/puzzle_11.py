from itertools import product

def count_flashes(input, steps):
    """
    >>> input = "5483143223\\n2745854711\\n5264556173\\n6141336146\\n6357385478\\n4167524645\\n2176841721\\n6882881134\\n4846848554\\n5283751526"
    >>> count_flashes(input, 10)
    204
    """
    input = [[int(c) for c in r] for r in input.split('\n')]
    total = 0
    while steps:
        input = _update_input(input)
        total += sum(1 for r, c in product(range(len(input)), repeat = 2) if input[r][c] == 0)
        steps -= 1
    return total


def count_synchronous_flashes(input):
    """
    >>> input = "5483143223\\n2745854711\\n5264556173\\n6141336146\\n6357385478\\n4167524645\\n2176841721\\n6882881134\\n4846848554\\n5283751526"
    >>> count_synchronous_flashes(input)
    195
    """
    input = [[int(c) for c in r] for r in input.split('\n')]
    steps = 0
    while any(input[r][c] != 0 for r, c in product(range(len(input)), repeat = 2)):
        steps += 1
        input = _update_input(input)
    return steps


def _update_input(input):
    input = input[:]
    flashes = set()
    def update_point(r, c):
        if input[r][c] == 9 and (r, c) not in flashes:
            flashes.add((r, c))
            for i, j in product((-1, 0, 1), (-1, 0, 1)):
                if r + i in range(0, len(input)) and c + j in range(0, len(input)):
                    update_point(r + i, c + j)
        else:
            input[r][c] = (input[r][c] + 1) % 10
    for r, c in product(range(len(input)), repeat = 2):
        update_point(r, c)
    for r, c in flashes:
        input[r][c] = 0
    return input


if __name__ == "__main__":
    import doctest; doctest.testmod()
    with open("input.txt") as f:
        input = f.read().strip()
        print(f"Solution to Puzzle 11, Part A: {count_flashes(input, 100)}")  # should equal 1615
        print(f"Solution to Puzzle 11, Part B: {count_synchronous_flashes(input)}")  # should equal 249
