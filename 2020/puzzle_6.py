from functools import reduce
from string import ascii_lowercase

def solve(groups):
    part_a = sum(len(reduce(lambda a, c: a | set(c), group, set())) for group in groups)
    part_b = sum(len(reduce(lambda a, c: a & set(c), group, set(ascii_lowercase))) for group in groups)
    return part_a, part_b


if __name__ == '__main__':
    with open('./input/input_6.txt') as f:
        groups = [g.split('\n') for g in f.read().strip().split('\n\n')]
    part_a, part_b = solve(groups)
    print(part_a)  # 6703
    print(part_b)  # 3430
