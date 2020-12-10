from functools import reduce

def part_a(timestamp, ids):
    """
    >>> part_a(939, [7, 13, 59, 31, 19])
    295
    """
    delays = {i: i * (1 + timestamp // i) - timestamp for i in ids}
    min_delay = min(delays, key=delays.get)
    return min_delay * delays[min_delay]


def part_b(times):
    """
    >>> part_b([7, 13, None, None, 59, None, 31, 19])
    1068781

    >>> part_b([17, None, 13, 19])
    3417

    >>> part_b([67, 7, 59, 61])
    754018

    >>> part_b([67, None, 7, 59, 61])
    779210

    >>> part_b([67, 7, None, 59, 61])
    1261476

    >>> part_b([1789, 37, 47, 1889])
    1202161486
    """
    def find_base(seed, step, p, offset):
        while (seed + offset) % p != 0:
            seed += step
        return seed
    offsets = {time: offset for offset, time in enumerate(times) if time}
    times = sorted(offsets.keys(), reverse=True)
    def reducer(a, c):
        seed, step = a
        return find_base(seed, step, c, offsets[c] - offsets[times[0]]), step * c
    return reduce(reducer, times, (0, 1))[0] - offsets[times[0]]


if __name__ == '__main__':
    # doctests
    import doctest; doctest.testmod()

    # part A
    data = "1000655\n17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,571,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,401,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19"
    timestamp = int(data.split('\n')[0])
    ids = list(map(int, filter(lambda c: c.isnumeric(), data.split('\n')[1].split(','))))
    print(part_a(timestamp, ids))  # 138

    # part B
    times = [int(c) if c.isnumeric() else None for c in data.split('\n')[1].split(',')]
    print(part_b(times))  # 226845233210288
