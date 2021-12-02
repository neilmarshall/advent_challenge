def count_increases(measurements):
    """
    >>> count_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    7
    """
    return sum(1 for fst, snd in zip(measurements, measurements[1:]) if snd > fst)


def count_window_increases(measurements):
    """
    >>count_window_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    5
    """
    windows = [sum(measurements[i:i+3]) for i in range(len(measurements) - 2)]
    return sum(1 for fst, snd in zip(windows, windows[1:]) if snd > fst)


if __name__ == "__main__":
    import doctest; doctest.testmod()
    with open("puzzle_1.txt") as f:
        measurements = list(map(int, f.readlines()))
        print(f"Solution to Puzzle 1, Part A: {count_increases(measurements)}")
        print(f"Solution to Puzzle 1, Part B: {count_window_increases(measurements)}")
