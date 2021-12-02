def parse_directions(directions):
    """
    >>> parse_directions(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"])
    150
    """
    pass
    H, D = 0, 0
    for direction in directions:
        action, value = direction.split()[0][0], int(direction.split()[1])
        if action == "f":
            H += value
        elif action == "d":
            D += value
        elif action == "u":
            D -= value
        else:
            raise ValueError(f"Unrecognized Input: {direction}")
    return H * D


def parse_directions_advanced(directions):
    """
    >>> parse_directions_advanced(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"])
    900
    """
    pass
    H, D, A = 0, 0, 0
    for direction in directions:
        action, value = direction.split()[0][0], int(direction.split()[1])
        if action == "f":
            H += value
            D += value * A
        elif action == "d":
            A += value
        elif action == "u":
            A -= value
        else:
            raise ValueError(f"Unrecognized Input: {direction}")
    return H * D


if __name__ == "__main__":
    import doctest; doctest.testmod()
    with open("puzzle_2.txt") as f:
        directions = f.readlines()
        print(f"Solution to Puzzle 1, Part A: {parse_directions(directions)}")
        print(f"Solution to Puzzle 1, Part B: {parse_directions_advanced(directions)}")
