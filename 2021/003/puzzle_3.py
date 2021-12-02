def parse_diagnostics(diagnostics):
    """
    >>> parse_diagnostics(["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"])
    198
    """
    bits = {i: {'0': 0, '1': 0} for i in range(len(diagnostics[0]))}
    for diagnostic in diagnostics:
        for i, d in enumerate(diagnostic):
            bits[i][d] += 1
    gamma = ''
    for i in range(len(diagnostics[0])):
        if bits[i]['0'] > bits[i]['1']:
            gamma += '0'
        else:
            gamma += '1'
    epsilon = int(''.join('1' if c == '0' else '0' for c in gamma), base = 2)
    gamma = int(gamma, base = 2)
    return gamma * epsilon


def parse_diagnostics_advanced(diagnostics):
    """
    >>> parse_diagnostics_advanced(["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"])
    230
    """
    def get_oxygen_generator_rating(diagnostics, bit = 0):
        if len(diagnostics) == 1:
            return diagnostics[0]
        zero_bits = sum(1 for d in diagnostics if d[bit] == '0')
        nonzero_bits = len(diagnostics) - zero_bits
        if zero_bits > nonzero_bits:
            return get_oxygen_generator_rating([d for d in diagnostics if d[bit] == '0'], bit + 1)
        return get_oxygen_generator_rating([d for d in diagnostics if d[bit] == '1'], bit + 1)
    def get_co2_scrubber_rating(diagnostics, bit = 0):
        if len(diagnostics) == 1:
            return diagnostics[0]
        zero_bits = sum(1 for d in diagnostics if d[bit] == '0')
        nonzero_bits = len(diagnostics) - zero_bits
        if zero_bits <= nonzero_bits:
            return get_co2_scrubber_rating([d for d in diagnostics if d[bit] == '0'], bit + 1)
        return get_co2_scrubber_rating([d for d in diagnostics if d[bit] == '1'], bit + 1)
    oxygen_generator_rating = get_oxygen_generator_rating(diagnostics)
    co2_scrubber_rating = get_co2_scrubber_rating(diagnostics)
    return int(oxygen_generator_rating, base = 2) * int(co2_scrubber_rating, base = 2)


if __name__ == "__main__":
    import doctest; doctest.testmod()
    with open("input.txt") as f:
        diagnostics = [r.strip() for r in f.readlines()]
        print(f"Solution to Puzzle 3, Part A: {parse_diagnostics(diagnostics)}")
        print(f"Solution to Puzzle 3, Part B: {parse_diagnostics_advanced(diagnostics)}")
