"""Advent of Code 2025 - Puzzle 1 - https://adventofcode.com/2025/day/1"""
if __name__ == "__main__":
    with open('input.txt', 'r', encoding='utf-8') as f:
        current_position, origin_hit_count = 50, 0
        for row in f:
            direction, value = row[0], row[1:]
            if direction == "L":
                current_position -= int(value)
            elif direction == "R":
                current_position += int(value)
            else:
                raise ValueError(f"Invalid direction: {direction}")
            current_position %= 100
            if current_position == 0:
                origin_hit_count += 1
    print(f"Solution to Part A: {origin_hit_count}")  # expected output is 1,147
    with open('input.txt', 'r', encoding='utf-8') as f:
        current_position, origin_hit_count = 50, 0
        for row in f:
            direction, value = row[0], int(row[1:])
            if value >= 100:
                origin_hit_count += value // 100
                value %= 100
            if direction == "L":
                if current_position != 0 and value >= current_position:
                    origin_hit_count += 1
                current_position -= value
            elif direction == "R":
                if current_position != 0 and value + current_position >= 100:
                    origin_hit_count += 1
                current_position += value
            else:
                raise ValueError(f"Invalid direction: {direction}")
            current_position %= 100
    print(f"Solution to Part B: {origin_hit_count}")  # expected output is 6,789
