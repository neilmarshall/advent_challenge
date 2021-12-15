from heapq import heappush, heappop
from itertools import count, product
from math import inf

class PriorityQueue():
    """An implementation of a priority queue - take from https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes"""
    @staticmethod
    @property
    def REMOVED():
        return '<removed-task>'  # placeholder for a removed task

    def __init__(self):
        self.pq = []            # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of tasks to entries
        self.counter = count()  # unique sequence count

    def add_task(self, task, priority=0):
        '''Add a new task or update the priority of an existing task'''
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        '''Mark an existing task as REMOVED.  Raise KeyError if not found.'''
        entry = self.entry_finder.pop(task)
        entry[-1] = PriorityQueue.REMOVED

    def pop_task(self):
        '''Remove and return the lowest priority task. Raise KeyError if empty.'''
        while self.pq:
            _, _, task = heappop(self.pq)
            if task is not PriorityQueue.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')


def djikstra(graph):
    """
    >>> graph = [[1,1,6,3,7,5,1,7,4,2], [1,3,8,1,3,7,3,6,7,2], [2,1,3,6,5,1,1,3,2,8], [3,6,9,4,9,3,1,5,6,9], [7,4,6,3,4,1,7,1,1,1], [1,3,1,9,1,2,8,1,3,7], [1,3,5,9,9,1,2,4,2,1], [3,1,2,5,4,2,1,6,3,9], [1,2,9,3,1,3,8,5,2,1], [2,3,1,1,9,4,4,5,8,1]]
    >>> djikstra(graph)
    40

    >>> djikstra(extend_grid(graph, 5))
    315
    """
    def get_unvisited_neighbours(node):
        p0, p1 = node
        if (p0 - 1, p1) in unvisited: yield (p0 - 1, p1)
        if (p0 + 1, p1) in unvisited: yield (p0 + 1, p1)
        if (p0, p1 - 1) in unvisited: yield (p0, p1 - 1)
        if (p0, p1 + 1) in unvisited: yield (p0, p1 + 1)

    pq = PriorityQueue()
    unvisited = {(r, c): inf if r > 0 or c > 0 else 0 for r, c in product(range(len(graph)), repeat=2)}
    for r in range(len(graph)):
        for c in range(len(graph)):
            pq.add_task((r, c), priority=inf)
    pq.add_task((0, 0), priority=0)
    while True:
        curr_node = pq.pop_task()
        curr_dist = unvisited.pop(curr_node)
        for neighbour in get_unvisited_neighbours(curr_node):
            unvisited[neighbour] = min(unvisited[neighbour], curr_dist + graph[neighbour[0]][neighbour[1]])
            pq.add_task(neighbour, priority=unvisited[neighbour])
        if curr_node == (len(graph) - 1, len(graph) - 1):
            return curr_dist

    
def extend_grid(grid, repeats):
    """
    >>> extend_grid([[1, 2, 3], [7, 8, 9], [9, 5, 8]], 3)
    [[1, 2, 3, 2, 3, 4, 3, 4, 5], [7, 8, 9, 8, 9, 1, 9, 1, 2], [9, 5, 8, 1, 6, 9, 2, 7, 1], [2, 3, 4, 3, 4, 5, 4, 5, 6], [8, 9, 1, 9, 1, 2, 1, 2, 3], [1, 6, 9, 2, 7, 1, 3, 8, 2], [3, 4, 5, 4, 5, 6, 5, 6, 7], [9, 1, 2, 1, 2, 3, 2, 3, 4], [2, 7, 1, 3, 8, 2, 4, 9, 3]]
    """
    new_grid = [[0 for _ in range(len(grid) * repeats)] for _ in range(len(grid) * repeats)]
    for r in range(len(new_grid)):
        for c in range(len(new_grid)):
            if r < len(grid) and c < len(grid):
                new_grid[r][c] = grid[r][c]
            elif r < len(grid):
                new_grid[r][c] = (grid[r][c % len(grid)] + (c // len(grid)) - 1) % 9 + 1
            else:
                new_grid[r][c] = (new_grid[r % len(grid)][c] + (r // len(grid)) - 1) % 9 + 1
    return new_grid


if __name__ == '__main__':
    import doctest; doctest.testmod()
    with open('input.txt') as f:
        grid = [[*map(int, l.strip())] for l in f.readlines()]
    print(f"Solution to problem 15, part A: {djikstra(grid)}")  # should equal 423
    print(f"Solution to problem 15, part A: {djikstra(extend_grid(grid, 5))}")  # should equal 2778