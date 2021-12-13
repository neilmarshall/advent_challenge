from itertools import dropwhile, takewhile

def count_visible_dots(instructions, steps):
    """
    >>> instructions = ["6,10", "0,14", "9,10", "0,3", "10,4", "4,11", "6,0", "6,12", "4,1", "0,13", "10,12", "3,4", "3,0", "8,4", "1,10", "2,14", "8,10", "9,0", "", "fold along y=7", "fold along x=5"]
    >>> grid = count_visible_dots(instructions, 1)
    >>> sum(1 for r in grid for c in r if c == '#')
    17

    >>> grid = count_visible_dots(instructions, 2)
    >>> sum(1 for r in grid for c in r if c == '#')
    16
    """
    grid_instructions = [*(tuple(map(int, row.split(','))) for row in takewhile(lambda instruction: instruction != "", instructions))]
    fold_instructions = [*dropwhile(lambda instruction: instruction != "", instructions)][1:]
    height, width = max(instruction[1] for instruction in grid_instructions) + 1, max(instruction[0] for instruction in grid_instructions) + 1
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for c, r in grid_instructions:
        grid[r][c] = '#'
    for fold_instruction in fold_instructions:
        if steps is not None and steps == 0:
            break
        if fold_instruction.startswith('fold along x='):
            x = int(fold_instruction.split('=')[-1])
            for r in range(len(grid)):
                for c in range(x):
                    if grid[r][c] == '#' or (grid[r][-c] if len(grid[0]) % 2 == 0 else grid[r][-(c + 1)]) == '#':
                        grid[r][c] = '#'
            grid = [g[:x] for g in grid]
        elif fold_instruction.startswith('fold along y='):
            y = int(fold_instruction.split('=')[-1])
            for c in range(len(grid[0])):
                for r in range(y):
                    if grid[r][c] == '#' or (grid[-r][c] if len(grid) % 2 == 0 else grid[-(r + 1)][c]) == '#':
                        grid[r][c] = '#'
            grid = grid[:y]
        if steps is not None:
            steps -= 1
    return grid


if __name__ == "__main__":
    import doctest; doctest.testmod()
    with open('input.txt') as f:
        instructions = f.read().split('\n')
        print(f"Solution to Puzzle 13, Part A: {sum(1 for r in count_visible_dots(instructions, 1) for c in r if c == '#')}")  # should equal 737
        print("Solution to Puzzle 13, Part B:\n")  # should equal ZUJUAFHP
        for g in count_visible_dots(instructions, None):
            print(f"\t{''.join(g)}")