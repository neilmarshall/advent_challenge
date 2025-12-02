"""Advent of Code 2025 - Puzzle 2 - https://adventofcode.com/2025/day/2"""
# pylint: disable=line-too-long

PUZZLE_INPUT = "3737332285-3737422568,5858547751-5858626020,166911-236630,15329757-15423690,753995-801224,1-20,2180484-2259220,24-47,73630108-73867501,4052222-4199117,9226851880-9226945212,7337-24735,555454-591466,7777695646-7777817695,1070-2489,81504542-81618752,2584-6199,8857860-8922218,979959461-980003045,49-128,109907-161935,53514821-53703445,362278-509285,151-286,625491-681593,7715704912-7715863357,29210-60779,3287787-3395869,501-921,979760-1021259"

if __name__ == "__main__":
    # part A
    valid_ids = []
    for rng in PUZZLE_INPUT.split(","):
        start, end = map(int, rng.split("-"))
        for i in range(start, end + 1):
            for j in range(1, len(str(i)) // 2 + 1):
                if str(i)[:j] == str(i)[j:]:
                    valid_ids.append(i)
    print(f"Solution to Part A: {sum(valid_ids)}")  # solution to part A: 38437576669

    # part B
    valid_ids = set()
    for rng in PUZZLE_INPUT.split(","):
        start, end = map(int, rng.split("-"))
        for i in range(start, end + 1):
            for j in range(1, len(str(i)) // 2 + 1):
                if len(str(i)) % j == 0:
                    if len(set(str(i)[k:k+j] for k in range(0, len(str(i))+1, j) if str(i)[k:k+j] != '')) == 1:
                        valid_ids.add(i)
    print(f"Solution to Part B: {sum(valid_ids)}")  # solution to part B: 49046150754
