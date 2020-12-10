from collections import namedtuple

Seat = namedtuple('Seat', ['row', 'col', 'id'])

def parse_seat(code):
    """
    >>> parse_seat("FBFBBFFRLR")
    Seat(row=44, col=5, id=357)

    >>> parse_seat("BFFFBBFRRR")
    Seat(row=70, col=7, id=567)

    >>> parse_seat("FFFBBBFRRR")
    Seat(row=14, col=7, id=119)

    >>> parse_seat("BBFFBBFRLL")
    Seat(row=102, col=4, id=820)
    """
    def parse_section(code, key1, key2, s, e):
        if not code:
            return s
        if code[0] == key1:
            return parse_section(code[1:], key1, key2, s, (s + e) // 2)
        if code[0] == key2:
            return parse_section(code[1:], key1, key2, (s + e) // 2 + 1, e)
    row, col = parse_section(code[:7], 'F', 'B', 0, 127), parse_section(code[-3:], 'L', 'R', 0, 7)
    return Seat(row, col, row * 8 + col)


if __name__ == '__main__':
    import doctest; doctest.testmod()
    with open('./input/input_5.txt') as f:
        ids = set(seat.id for seat in map(parse_seat, (row.strip() for row in f.readlines())))
    print(max(ids))  # should be 938
    print(next(id + 1 for id in ids if id + 1 not in ids))  # should be 696
