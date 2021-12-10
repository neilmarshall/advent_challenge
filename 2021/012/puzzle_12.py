def count_paths(routes, allow_duplicates=False):
    """
    >>> routes = ["start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"]
    >>> count_paths(routes)
    10

    >>> count_paths(routes, True)
    36

    >>> routes = ["dc-end", "HN-start", "start-kj", "dc-start", "dc-HN", "LN-dc", "HN-end", "kj-sa", "kj-HN", "kj-dc"]
    >>> count_paths(routes)
    19

    >>> count_paths(routes, True)
    103

    >>> routes = ["fs-end", "he-DX", "fs-he", "start-DX", "pj-DX", "end-zg", "zg-sl", "zg-pj", "pj-he", "RW-he", "fs-DX", "pj-RW", "zg-RW", "start-pj", "he-WI", "zg-he", "pj-fs", "start-RW"]
    >>> count_paths(routes)
    226

    >>> count_paths(routes, True)
    3509
    """
    nodes = {}
    for p0, p1 in (r.split('-') for r in routes):
        if p0 not in nodes:
            nodes[p0] = []
        nodes[p0].append(p1)
        if p1 not in nodes:
            nodes[p1] = []
        nodes[p1].append(p0)
    def get_routes_from(location, visited_small_caves):
        total = 0
        for route in nodes[location]:
            if route == 'end':
                total += 1
            elif route != 'start':
                if visited_small_caves.get(route, 0) == 0 or (allow_duplicates and 2 not in visited_small_caves.values() and visited_small_caves.get(route, 0) == 1):
                    total += get_routes_from(route, visited_small_caves | ({route: visited_small_caves.get(route, 0) + 1} if route.islower() else {}))
        return total
    return get_routes_from('start', {})


if __name__ == "__main__":
    import doctest; doctest.testmod()
    with open('input.txt') as f:
        routes = [*map(str.strip, f.readlines())]
        print(f"Solution to Puzzle 12, Part A: {count_paths(routes)}")  # should equal 3497
        print(f"Solution to Puzzle 12, Part B: {count_paths(routes, True)}")  # should equal 93686
