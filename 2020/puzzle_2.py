import re

# part (a)
def part_a():
    with open('./input/input_2.txt') as f:
        data = f.readlines()
    def is_valid(row):
        match = re.match(r'^(?P<lower>\d+)-(?P<upper>\d+) (?P<char>[a-z]): (?P<password>[a-z]+)$', row)
        lower, upper = [int(match.group(label)) for label in ('lower', 'upper')]
        char, password = [match.group(label) for label in ('char', 'password')]
        return password.count(char) in range(lower, upper + 1)
    print(sum(1 for row in data if is_valid(row)))

# part (b)
def part_b():
    with open('./input/input_2.txt') as f:
        data = f.readlines()
    def is_valid(row):
        match = re.match(r'^(?P<first>\d+)-(?P<second>\d+) (?P<char>[a-z]): (?P<password>[a-z]+)$', row)
        first, second = [int(match.group(label)) for label in ('first', 'second')]
        char, password = [match.group(label) for label in ('char', 'password')]
        return (password[first - 1] == char and password[second - 1] != char) or (password[first - 1] != char and password[second - 1] == char)
    print(sum(1 for row in data if is_valid(row)))

if __name__ == '__main__':
    part_a()
    part_b()
