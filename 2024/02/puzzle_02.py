"""Solution to Problem 2, 2024"""

def is_safe(report : list[int]) -> bool:
    """
    Compute if a given report is safe, i.e. all ascending or descending, and
    with max difference between elements at most 3.
    """
    if any(abs(x - y) > 3 for x, y in zip(report[1:], report)):
        return False
    is_ascending = all(x > y for x, y in zip(report[1:], report))
    is_descending = all(x < y for x, y in zip(report[1:], report))
    return is_ascending or is_descending

def is_safe_with_dampener(report : list[int]) -> bool:
    """
    Compute if a given report is safe with allowance for a dampener - achieved by checking
    each possible sub-report and running it through the basic 'is_safe' algorithm.
    """
    for i in range(len(report)):
        subreport = report[:i] + report[i+1:]
        if is_safe(subreport):
            return True
    return False

if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        data = [list(map(int, line.split(' '))) for line in f.readlines()]

    # compute solution to part A - should be 490
    print(len(list(filter(is_safe, data))))

    # compute solution to part B - should be 536
    print(len(list(filter(is_safe_with_dampener, data))))
