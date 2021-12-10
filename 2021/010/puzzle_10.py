def check_line(line):
    """
    >>> check_line("{([(<{}[<>[]}>{[]{[(<()>")
    1197

    >>> check_line("[[<[([]))<([[{}[[()]]]")
    3

    >>> check_line("[{[{({}]{}}([{[{{{}}([]")
    57

    >>> check_line("[<(<(<(<{}))><([]([]()")
    3

    >>> check_line("<{([([[(<>()){}]>(<<{{")
    25137
    """
    opening_tags = set(('(', '{', '[', '<'))
    stack = []
    for c in line:
        if c in opening_tags:
            stack.append(c)
        else:
            t = {')': '(', '}': '{', ']': '[', '>': '<'}[c]
            if t != stack[-1]:
                return {')': 3, '}': 1197, ']': 57, '>': 25137}[c]
            else:
                stack.pop()
    return 0


def score_syntax_errors(input):
    """
    >>> input = ["[({(<(())[]>[[{[]{<()<>>", "[(()[<>])]({[<{<<[]>>(", "{([(<{}[<>[]}>{[]{[(<()>", "(((({<>}<{<{<>}{[]{[]{}", "[[<[([]))<([[{}[[()]]]", "[{[{({}]{}}([{[{{{}}([]", "{<[[]]>}<{[{[{[]{()[[[]", "[<(<(<(<{}))><([]([]()", "<{([([[(<>()){}]>(<<{{", "<{([{{}}[<[[[<>{}]]]>[]]"]
    >>> score_syntax_errors(input)
    26397
    """
    return sum(map(check_line, input))


def complete_line(line):
    """
    >>> complete_line("[({(<(())[]>[[{[]{<()<>>")
    288957

    >>> complete_line("[(()[<>])]({[<{<<[]>>(")
    5566

    >>> complete_line("(((({<>}<{<{<>}{[]{[]{}")
    1480781

    >>> complete_line("{<[[]]>}<{[{[{[]{()[[[]")
    995444

    >>> complete_line("<{([{{}}[<[[[<>{}]]]>[]]")
    294
    """
    opening_tags = set(('(', '{', '[', '<'))
    stack = []
    for c in line:
        if c in opening_tags:
            stack.append(c)
        else:
            t = {')': '(', '}': '{', ']': '[', '>': '<'}[c]
            if t != stack[-1]:
                return {')': 3, '}': 1197, ']': 57, '>': 25137}[c]
            else:
                stack.pop()
    line_completion = ''.join({'(': ')', '{': '}', '[': ']', '<': '>'}[c] for c in stack[::-1])
    total = 0
    for c in line_completion:
        total = (total * 5) + {')': 1, ']': 2, '}': 3, '>': 4}[c]
    return total


def score_line_completions(input):
    """
    >>> score_line_completions(["[({(<(())[]>[[{[]{<()<>>", "[(()[<>])]({[<{<<[]>>(", "{([(<{}[<>[]}>{[]{[(<()>", "(((({<>}<{<{<>}{[]{[]{}", "[[<[([]))<([[{}[[()]]]", "[{[{({}]{}}([{[{{{}}([]", "{<[[]]>}<{[{[{[]{()[[[]", "[<(<(<(<{}))><([]([]()", "<{([([[(<>()){}]>(<<{{", "<{([{{}}[<[[[<>{}]]]>[]]"])
    288957
    """
    valid_lines = [line for line in input if check_line(line) == 0]
    scores = sorted(map(complete_line, valid_lines))
    return scores[len(scores) // 2]


if __name__ == "__main__":
    import doctest; doctest.testmod()
    with open("input.txt") as f:
        input = [*map(str.strip, f.readlines())]
    print(f"Solution to Puzzle 10, Part A: {score_syntax_errors(input)}")  # should equal 411471
    print(f"Solution to Puzzle 10, Part B: {score_line_completions(input)}")  # should equal 3122628974