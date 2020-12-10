from collections import Counter
from functools import reduce
from itertools import chain

def count_chain_gaps(data):
    """
    >>> count_chain_gaps([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
    35

    >>> count_chain_gaps([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3])
    220
    """
    data = list(chain((0,), sorted(data), (max(data) + 3,)))
    counter = Counter(a - b for a, b in zip(data[1:], data))
    return counter[1] * counter[3]


def count_arrangements(data):
    """
    >>> count_arrangements([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
    8

    >>> count_arrangements([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3])
    19208
    """
    reducer = lambda a, c: {c: sum(a[c + i] for i in range(1, 4) if c + i in a)} | a
    return reduce(reducer, chain(sorted(data, reverse=True), (0,)), {max(data) + 3: 1})[0]


if __name__ == '__main__':
    import doctest; doctest.testmod()
    with open("./input/input_10.txt") as f:
        data = list(map(int, f.readlines()))
    print(f"{count_chain_gaps(data):,d}")  # 1,920
    print(f"{count_arrangements(data):,d}")  # 1,511,207,993,344