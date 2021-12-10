from functools import reduce

def reduce_stack(line):
    opening_tags = set(('(', '{', '[', '<'))
    stack = []
    for c in line:
        if c in opening_tags:
            stack.append(c)
        else:
            if {')': '(', '}': '{', ']': '[', '>': '<'}[c] != stack[-1]:
                return stack, c
            else:
                stack.pop()
    return stack, None


def score_syntax_errors(input):
    """
    >>> score_syntax_errors(["[({(<(())[]>[[{[]{<()<>>", "[(()[<>])]({[<{<<[]>>(", "{([(<{}[<>[]}>{[]{[(<()>", "(((({<>}<{<{<>}{[]{[]{}", "[[<[([]))<([[{}[[()]]]", "[{[{({}]{}}([{[{{{}}([]", "{<[[]]>}<{[{[{[]{()[[[]", "[<(<(<(<{}))><([]([]()", "<{([([[(<>()){}]>(<<{{", "<{([{{}}[<[[[<>{}]]]>[]]"])
    26397
    """
    scorer = lambda c: {')': 3, '}': 1197, ']': 57, '>': 25137}.get(c, 0)
    return sum(scorer(c) for _, c in map(reduce_stack, input) if c is not None)


def score_line_completions(input):
    """
    >>> score_line_completions(["[({(<(())[]>[[{[]{<()<>>", "[(()[<>])]({[<{<<[]>>(", "{([(<{}[<>[]}>{[]{[(<()>", "(((({<>}<{<{<>}{[]{[]{}", "[[<[([]))<([[{}[[()]]]", "[{[{({}]{}}([{[{{{}}([]", "{<[[]]>}<{[{[{[]{()[[[]", "[<(<(<(<{}))><([]([]()", "<{([([[(<>()){}]>(<<{{", "<{([{{}}[<[[[<>{}]]]>[]]"])
    288957
    """
    def complete_line(line):
        line_completion = ''.join({'(': ')', '{': '}', '[': ']', '<': '>'}[c] for c in line[::-1])
        return reduce(lambda a, c: (a * 5) + {')': 1, ']': 2, '}': 3, '>': 4}[c], line_completion, 0)
    scores = sorted(complete_line(s) for s, c in map(reduce_stack, input) if c is None)
    return scores[len(scores) // 2]


if __name__ == "__main__":
    import doctest; doctest.testmod()
    with open("input.txt") as f:
        input = [*map(str.strip, f.readlines())]
    print(f"Solution to Puzzle 10, Part A: {score_syntax_errors(input)}")  # should equal 411471
    print(f"Solution to Puzzle 10, Part B: {score_line_completions(input)}")  # should equal 3122628974
