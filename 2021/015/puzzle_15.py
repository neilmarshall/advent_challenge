from pprint import pprint

def minimise_path(risk_levels):
    """
    >>> risk_levels = [[1,1,6,3,7,5,1,7,4,2], [1,3,8,1,3,7,3,6,7,2], [2,1,3,6,5,1,1,3,2,8], [3,6,9,4,9,3,1,5,6,9], [7,4,6,3,4,1,7,1,1,1], [1,3,1,9,1,2,8,1,3,7], [1,3,5,9,9,1,2,4,2,1], [3,1,2,5,4,2,1,6,3,9], [1,2,9,3,1,3,8,5,2,1], [2,3,1,1,9,4,4,5,8,1]]
    >>> minimise_path(risk_levels)
    40
    """
    def djikstra(risk_levels, start, end):
        def get_neighbours(point):
            p0, p1 = point
            # yield (p0 - 1, p1)
            yield (p0 + 1, p1)
            # yield (p0, p1 - 1)
            yield (p0, p1 + 1)
        # risk_map = {(p0, p1): None for p0 in range(len(risk_levels)) for p1 in range(len(risk_levels))}
        risk_map = {(p0, p1): 100000 for p0 in range(len(risk_levels)) for p1 in range(len(risk_levels))}
        e0, e1 = start
        risk_map[(e0, e1)] = risk_levels[e0][e1]
        unvisited = set(get_neighbours(start))
        pprint(risk_map)
        print(unvisited)
        while unvisited:
            point = unvisited.pop()
            if point in risk_map:
                neighbours = [*filter(lambda n: n in risk_map, get_neighbours(point))]
                # print(point, neighbours)
                risk_map[point] = risk_levels[point[0]][point[1]] + min(risk_map[n] for n in neighbours if risk_map[n] is not None)
                for n in neighbours:
                    if risk_map[n] is None:
                        unvisited.add(n)
        pprint(risk_map)
    return djikstra(risk_levels, (0, 0), (len(risk_levels) - 1, len(risk_levels) - 1))


if __name__ == "__main__":
    import doctest; doctest.testmod()
