"""Solution to Problem 7, 2024"""

# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest

class EquationIsValidFixture(unittest.TestCase):
    def test_equation_is_valid(self):
        test_cases = [
            (190, [10, 19], True),
            (3267, [81, 40, 27], True),
            (83, [17, 5], False),
            (156, [15, 6], False),
            (7290, [6, 8, 6, 15], False),
            (161011, [16, 10, 13], False),
            (192, [17, 8, 14], False),
            (21037, [9, 7, 18, 13], False),
            (292, [11, 6, 16, 20], True),
        ]
        for test_case in test_cases:
            target, values, expectation = test_case
            with self.subTest(target=target, values=values):
                self.assertEqual(equation_is_valid(target, values), expectation)

    def test_equation_is_valid_with_concatenation(self):
        test_cases = [
            (190, [10, 19], True),
            (3267, [81, 40, 27], True),
            (83, [17, 5], False),
            (156, [15, 6], True),
            (7290, [6, 8, 6, 15], True),
            (161011, [16, 10, 13], False),
            (192, [17, 8, 14], True),
            (21037, [9, 7, 18, 13], False),
            (292, [11, 6, 16, 20], True),
        ]
        for test_case in test_cases:
            target, values, expectation = test_case
            with self.subTest(target=target, values=values):
                self.assertEqual(equation_is_valid(target, values, True), expectation)

def equation_is_valid(target: int, values : list[int], allow_concatenation : bool = False) -> bool:
    assert len(values) > 0
    if len(values) == 1:
        return values[0] == target
    if allow_concatenation:
        if str(target) != str(values[-1]) and str(target).endswith(str(values[-1])):
            new_target = int(str(target)[:-len(str(values[-1]))])
            if equation_is_valid(new_target, values[:-1], allow_concatenation):
                return True
    if equation_is_valid(target - values[-1], values[:-1], allow_concatenation):
        return True
    if target % values[-1] != 0:
        return False
    return equation_is_valid(target // values[-1], values[:-1], allow_concatenation)

if __name__ == "__main__":
    unittest.main(exit=False)

    with open("input.txt", encoding="utf-8") as f:
        equations = []
        for line in f.readlines():
            head, tail = line.split(':', maxsplit=1)
            equations.append((int(head), list(map(int, tail.strip().split(' ')))))

    # compute solution to part A - should be 2437272016585
    print(sum(target for target, values in equations if equation_is_valid(target, values)))

    # compute solution to part B - should be 162987117690649
    print(sum(target for target, values in equations if equation_is_valid(target, values, True)))
