def solve1(grid):
    def execute(old_grid):
        new_grid = [row[:] for row in old_grid]
        state_changes = 0
        def get_neighbours(grid, r, c):
            neighbours = []
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if not (i == 0 and j == 0) and (r + i >= 0) and (c + j >= 0):
                        try:
                            neighbours.append(grid[r + i][c + j])
                        except IndexError:
                            pass
            return neighbours
        for r in range(len(new_grid)):
            for c in range(len(new_grid[0])):
                if old_grid[r][c] == 'L':
                    if sum(1 for cell in get_neighbours(old_grid, r, c) if cell == '#') == 0:
                        new_grid[r][c] = '#'
                        state_changes += 1
                if old_grid[r][c] == '#':
                    if sum(1 for cell in get_neighbours(old_grid, r, c) if cell == '#') >= 4:
                        new_grid[r][c] = 'L'
                        state_changes += 1
        if state_changes > 0:
            return execute(new_grid)
        return sum(1 for r in range(len(new_grid)) for c in range(len(new_grid[0])) if new_grid[r][c] == '#')
    return execute(grid)


def solve2(grid):
    def execute(old_grid):
        new_grid = [row[:] for row in old_grid]
        state_changes = 0
        def get_neighbours(grid, r, c):
            neighbours = []
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if not (i == 0 and j == 0):
                        try:
                            m = 1
                            while grid[r + m * i][c + m * j] == '.':
                                m += 1
                            if (r + m * i) >= 0 and (c + m * j >= 0):
                                neighbours.append(grid[r + m * i][c + m * j])
                        except IndexError:
                            pass
            return neighbours
        for r in range(len(new_grid)):
            for c in range(len(new_grid[0])):
                if old_grid[r][c] == 'L':
                    if sum(1 for cell in get_neighbours(old_grid, r, c) if cell == '#') == 0:
                        new_grid[r][c] = '#'
                        state_changes += 1
                if old_grid[r][c] == '#':
                    if sum(1 for cell in get_neighbours(old_grid, r, c) if cell == '#') >= 5:
                        new_grid[r][c] = 'L'
                        state_changes += 1
        if state_changes > 0:
            return execute(new_grid)
        return sum(1 for r in range(len(new_grid)) for c in range(len(new_grid[0])) if new_grid[r][c] == '#')
    return execute(grid)


if __name__ == '__main__':
    with open('./input/input_11.txt') as f:
        data = [list(row) for row in f.readlines()]
        print(solve1(data)) # 2346
        print(solve2(data))  # 2111
