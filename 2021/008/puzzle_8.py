from functools import reduce

def count_unique_segment_instances(input):
    """
    >>> input = []
    >>> input.append('be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe')
    >>> input.append('edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc')
    >>> input.append('fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg')
    >>> input.append('fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb')
    >>> input.append('aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea')
    >>> input.append('fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb')
    >>> input.append('dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe')
    >>> input.append('bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef')
    >>> input.append('egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb')
    >>> input.append('gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce')
    >>> input = '\\n'.join(input)
    >>> count_unique_segment_instances(input)
    26
    """
    segment_instances = [c for r in input.split('\n') for c in r.split('|')[-1].strip().split(' ')]
    return sum(1 for segment in segment_instances if len(segment) in (2, 4, 3, 7))


def parse_signal(input):
    """
    >>> parse_signal("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf")
    5353
    """
    # parse input
    signals, displays = input.split('|')[0].strip().split(' '), input.split('|')[1].strip().split(' ')

    # helper functions
    extractAll = lambda n: [set(e) for e in signals if len(e) == n]
    extractSingle = lambda n: [set(e) for e in signals if len(e) == n].pop()
    common = lambda sets: reduce(set.intersection, sets)

    # disjoint signal between len(2) and len(3) maps to display A
    A = (set(extractSingle(3)) - set(extractSingle(2))).pop()

    # common signals across len(5) and disjoint signals between len(4) and len(2) maps to display D
    D = common((common(extractAll(5)), (extractSingle(4) - extractSingle(2)))).pop()

    # len(4) less len(2) less signal mapped to D maps to display B
    B = (extractSingle(4) - extractSingle(2) - set(D)).pop()

    # common signals across len(5), less signals mapped to A and D maps to display G
    G = (common(extractAll(5)) - set(A) - set(D)).pop()

    # the one signal across len(5) that contains signals mapped to A, B, D and G leaves its remaining signal mapped to F
    F = (next(e for e in extractAll(5) if len(e & {A, B, D, G}) == 4) - {A, B, D, G}).pop()

    # disjoint signal between len(2) signal mapped to F maps to C
    C = (extractSingle(2) - set(F)).pop()

    # the residual signal maps to E
    E = (set('abcdefg') - {A, B, C, D, F, G}).pop()

    def parse_display(display):
        signal_from_display = { A: 'a', B: 'b', C: 'c', D: 'd', E: 'e', F: 'f', G: 'g' }
        code = ''.join(sorted(signal_from_display[s] for s in display))
        return { 'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9 }[code]

    return int(''.join(str(parse_display(d)) for d in displays))


def parse_signals(input):
    return sum(map(parse_signal, input.split('\n')))


if __name__ == "__main__":
    import doctest; doctest.testmod()
    with open("input.txt") as f:
        input = f.read()
    print(f"Solution to Puzzle 8, Part A: {count_unique_segment_instances(input)}")  # should equal 519
    print(f"Solution to Puzzle 8, Part B: {parse_signals(input)}")  # should equal 1027483