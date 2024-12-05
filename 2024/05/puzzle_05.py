"""Solution to Problem 5, 2024"""

import unittest

class SumUpdateMidpointsFixture(unittest.TestCase):
    page_ordering_rules = [
        (47, 53),
        (97, 13),
        (97, 61),
        (97, 47),
        (75, 29),
        (61, 13),
        (75, 53),
        (29, 13),
        (97, 29),
        (53, 29),
        (61, 53),
        (97, 53),
        (61, 29),
        (47, 13),
        (75, 47),
        (97, 75),
        (47, 61),
        (75, 61),
        (47, 29),
        (75, 13),
        (53, 13),
    ]

    updates = [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47]
    ]

    def test_sum_update_midpoints(self):
        self.assertEqual(sum_update_midpoints(self.page_ordering_rules, self.updates), (143, 123))

def sum_update_midpoints(page_ordering_rules : list[tuple[int, int]], updates : list[int]) -> int:
    predecessors, successors = {}, {}
    for predecessor, successor in page_ordering_rules:
        if predecessor not in successors:
            successors[predecessor] = set()
        successors[predecessor].add(successor)
        if successor not in predecessors:
            predecessors[successor] = set()
        predecessors[successor].add(predecessor)
    total_part_a = total_part_b = 0
    for update in updates:
        is_valid = True
        for i, e in enumerate(update):
            if e in predecessors and any(x in predecessors[e] for x in update[i + 1:]):
                is_valid = False
                break
            if e in successors and any(x in successors[e] for x in update[:i]):
                is_valid = False
                break
        if is_valid:
            total_part_a += update[len(update) // 2]
        else:
            elements = set(update)
            sorted_update = []
            while elements:
                element = next(e1 for e1 in elements if all(e2 in successors.get(e1, set()) or e2 == e1 for e2 in elements))
                elements.remove(element)
                sorted_update.append(element)
            total_part_b += sorted_update[len(update) // 2]
    return total_part_a, total_part_b

if __name__ == "__main__":
    unittest.main(exit=False)

    with open("input.txt", encoding="utf-8") as f:
        page_ordering_rules = []
        while True:
            row = f.readline()
            if row == '\n':
                break
            a, b = [int(x) for x in row.split('|')]
            page_ordering_rules.append((a, b))
        updates = []
        while True:
            row = f.readline()
            if row == '':
                break
            updates.append([int(x) for x in row.split(',')])

    solution_part_a, solution_part_b = sum_update_midpoints(page_ordering_rules, updates)

    # compute solution to part A - should be 6951
    print(solution_part_a)

    # compute solution to part B - should be 4121
    print(solution_part_b)
