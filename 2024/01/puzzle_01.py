"""Solution to Problem 1, 2024"""

from collections import Counter
from functools import reduce


def parse_input():
    """Parse input data."""
    def parse_data_point(element: str) -> tuple[int, int]:
        point_splits = element.split("   ")
        assert len(point_splits) == 2
        return int(point_splits[0].strip()), int(point_splits[1].strip())
    parsed_lists = ([], [])
    with open("input.txt", encoding="utf-8") as f:
        for element in f.readlines():
            parsed_data_point  = parse_data_point(element)
            assert len(parsed_data_point) == 2
            parsed_lists[0].append(parsed_data_point[0])
            parsed_lists[1].append(parsed_data_point[1])
    return parsed_lists

if __name__ == "__main__":
    lists = parse_input()

    # compute solution to part A - should be 2176849
    total_distance = reduce( \
        lambda a, c: a + abs(c[0] - c[1]), \
        zip(sorted(lists[0]), sorted(lists[1])), \
        0)
    print(total_distance)

    # compute solution to part A - should be 23384288
    counter = Counter(lists[1])
    similarity_score = reduce( \
        lambda a, c: a + c * counter.get(c, 0), \
        lists[0], \
        0)
    print(similarity_score)
