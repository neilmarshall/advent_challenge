"""Advent of Code 2025 - Puzzle 3 - https://adventofcode.com/2025/day/3"""
# pylint: disable=line-too-long

def get_joltage(bank : list[int], digit_count : int) -> int:
    """Get joltage for a given bank and digit count
    
    >>> rows = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']
    >>> banks = [[int(c) for c in row] for row in rows]
    >>> sum(get_joltage(bank, 2) for bank in banks)
    357
    >>> sum(get_joltage(bank, 12) for bank in banks)
    3121910778619
    """
    digits, idx = [], 0
    for i in range(digit_count - 1, -1, -1):
        bank_sub_range = bank[idx:-i] if i != 0 else bank[idx:]
        digits.append(max(bank_sub_range))
        idx += bank_sub_range.index(digits[-1]) + 1
    return int(str.join('', map(str, digits)))

if __name__ == "__main__":
    with open('input.txt', 'r', encoding='utf-8') as f:
        puzzle_input = [[int(c) for c in row.strip()] for row in f.readlines()]

    # part A
    print(f"Solution to Part A: {sum(get_joltage(bank, 2) for bank in puzzle_input)}")  # solution to part A: 17034

    # part B
    print(f"Solution to Part B: {sum(get_joltage(bank, 12) for bank in puzzle_input)}")  # solution to part B: 168798209663590
