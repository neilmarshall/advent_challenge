def score_bingo(numbers, boards):
    """
    >>> numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    >>> board1 = [[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]]
    >>> board2 = [[3, 15, 0, 2, 22], [9, 18, 13, 17, 5], [19, 8, 7, 25, 23], [20, 11, 10, 24, 4], [14, 21, 16, 12, 6]]
    >>> board3 = [[14, 21, 17, 24, 4], [10, 16, 15, 9, 19], [18, 8, 23, 26, 20], [22, 11, 13, 6, 5], [2, 0, 12, 3, 7]]
    >>> boards = [board1, board2, board3]
    >>> score_bingo(numbers, boards)
    4512
    """
    boards = _update_boards(boards, numbers[0])
    result = _check_boards(boards)
    if result is not None:
        return _score_board(result, numbers[0])
    return score_bingo(numbers[1:], boards)


def get_last_board(numbers, boards):
    """
    >>> numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    >>> board1 = [[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]]
    >>> board2 = [[3, 15, 0, 2, 22], [9, 18, 13, 17, 5], [19, 8, 7, 25, 23], [20, 11, 10, 24, 4], [14, 21, 16, 12, 6]]
    >>> board3 = [[14, 21, 17, 24, 4], [10, 16, 15, 9, 19], [18, 8, 23, 26, 20], [22, 11, 13, 6, 5], [2, 0, 12, 3, 7]]
    >>> boards = [board1, board2, board3]
    >>> get_last_board(numbers, boards)
    1924
    """
    remaining_boards = _eliminate_boards(_update_boards(boards, numbers[0]))
    if len(remaining_boards) == 1:
        for called in numbers:
            remaining_boards = _update_boards(remaining_boards, called)
            if _check_boards(remaining_boards) is not None:
                return _score_board(remaining_boards[0], called)
    return get_last_board(numbers[1:], remaining_boards)


def _update_boards(boards, called):
    return [[[c if c != called else None for c in r] for r in board] for board in boards]


def _check_board(board):
    return any(all(c is None for c in r) for r in board) or any(all(r[c] is None for r in board) for c in range(len(board)))


def _check_boards(boards):
    return next(filter(_check_board, boards), None)


def _score_board(board, n):
    return sum(c for r in board for c in r if c is not None) * n


def _eliminate_boards(boards):
    return [board for board in boards if not _check_board(board)]


if __name__ == "__main__":
    import doctest; doctest.testmod()
    with open("input.txt") as f:
        data = f.readlines()
    numbers = list(map(int, data[0].split(",")))
    boards = []
    for row in data[1:]:
        if row == "\n":
            boards.append([])
        else:
            boards[-1].append(list(map(int, row.split())))
    print(f"Solution to Puzzle 4, Part A: {score_bingo(numbers, boards)}")  # should equal 8442
    print(f"Solution to Puzzle 4, Part B: {get_last_board(numbers, boards)}")  # should equal 4590
