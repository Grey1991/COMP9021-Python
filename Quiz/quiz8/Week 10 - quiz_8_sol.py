# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by Eric Martin for COMP9021


import sys
from random import seed, choice
from array_queue import *

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()

def preferred_paths_to_corners():
    preferred_paths = {}
    moves = {'NE': ((1, -1), (1, 0), (0, -1)),
             'SE': ((1, 1), (1, 0), (0, 1)),
             'SW': ((-1, 1), (-1, 0), (0, 1)),
             'NW': ((-1, -1), (-1, 0), (0, -1))}
    paths = ArrayQueue()
    paths.enqueue([(size, size)])
    while not paths.is_empty():
        path = paths.dequeue()
        x, y = path[-1]
        if (x, y) in corners:
            if (x, y) not in preferred_paths:
                preferred_paths[(x, y)] = path
            continue
        for x_step, y_step in moves[grid[y][x]]:
            next_x, next_y = x + x_step, y + y_step
            if next_x < 0 or next_x >= dim or next_y < 0 or next_y >= dim:
                continue
            if (next_x, next_y) in path:
                continue
            extended_path = list(path)
            extended_path.append((next_x, next_y))
            paths.enqueue(extended_path)
    return preferred_paths

try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

for i in range(dim):
    for j in range(dim):
        grid[i][j] = choice(directions)
print('Here is the grid that has been generated:')
display_grid()

corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
paths = preferred_paths_to_corners()
if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print(f'There is no path to {corner}')
    else:
        print(f'The preferred path to {corner} is:')
        print('  ', paths[corner])
