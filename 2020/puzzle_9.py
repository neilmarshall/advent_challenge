def solve(data, p):
    """
    >>> solve([35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576], 5)
    (127, 62)
    """
    def is_valid(target, subset):
        return any(target - e in subset for e in subset)
    def find_contiguous_range(target):
        for i in range(len(data)):
            total = data[i]
            for j in range(i + 1, len(data)):
                total += data[j]
                if total == target:
                    return min(data[i:j+1]), max(data[i:j+1])
                if total > target:
                    continue
    weakness = next((data[d] for d in range(p, len(data)) if not is_valid(data[d], set(data[d - p : d]))))
    return weakness, sum(find_contiguous_range(weakness))


if __name__ == '__main__':
    import doctest; doctest.testmod()
    with open("./input/input_9.txt") as f:
        data = list(map(int, f.readlines()))
    print(solve(data, 25))  # (138879426, 23761694)
