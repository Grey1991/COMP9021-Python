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
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, choice
from array_queue import *


def display_grid():
    for i in range(dim):
        print('    ', end='')
        for j in range(dim):
            print(' ', grid[i][j], end='')
        print()
    print()


def preferred_paths_to_corners(grid,corner):
    # replace pass above with your code (aim for around 21 lines of code)
    def next_point(point):
        if point[0] - 1 >= 0:
            next_point1 = (point[0] - 1, point[1])
        else:
            next_point1 = None
        if point[0] - 1 >= 0 and point[1] + 1 <= 6:
            next_point2 = (point[0] - 1, point[1] + 1)
        else:
            next_point2 = None
        if point[1] + 1 <= 6:
            next_point3 = (point[0], point[1] + 1)
        else:
            next_point3 = None
        if point[1] + 1 <= 6 and point[0] + 1 <= 6:
            next_point4 = (point[0] + 1, point[1] + 1)
        else:
            next_point4 = None
        if point[0] + 1 <= 6:
            next_point5 = (point[0] + 1, point[1])
        else:
            next_point5 = None
        if point[0] + 1 <= 6 and point[1] - 1 >= 0:
            next_point6 = (point[0] + 1, point[1] - 1)
        else:
            next_point6 = None
        if point[1] - 1 >= 0:
            next_point7 = (point[0], point[1] - 1)
        else:
            next_point7 = None
        if point[0] - 1 >= 0 and point[1] - 1 >= 0:
            next_point8 = (point[0] - 1, point[1] - 1)
        else:
            next_point8 = None
        if grid[point[0]][point[1]] == 'NE':
            next_points = [next_point2, next_point3, next_point1]
        if grid[point[0]][point[1]] == 'SE':
            next_points = [next_point4, next_point3, next_point5]
        if grid[point[0]][point[1]] == 'SW':
            next_points = [next_point6, next_point7, next_point5]
        if grid[point[0]][point[1]] == 'NW':
            next_points = [next_point8, next_point7, next_point1]
        if point == (0, 0) or point == (0, 6) or point == (6, 0) or point == (6, 6):
            next_points = None
        return next_points

    s = set()
    d = {}
    L = []
    queue = ArrayQueue()
    queue.enqueue((3,3))
    s.add((3,3))
    while not queue.is_empty():
        current = queue.dequeue()
        if current == (corner[1],corner[0]):
            while current in d:
                L.append(d[current])
                current = d[current]
        else:
            next_points = next_point(current)
            if next_points:
                for i in next_points:
                    if i is not None and i not in s:
                        s.add(i)
                        queue.enqueue(i)
                        d[i] = current
    L = L[::-1]
    if L:
        L.append((corner[1],corner[0]))
    path = [(x[1],x[0]) for x in L]
    return path
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


corners = [(0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)]
path_num = 0
for corner in corners:
    path = preferred_paths_to_corners(grid, corner)
    if path:
        path_num += 1
if path_num ==0:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    path = preferred_paths_to_corners(grid, corner)
    if not path:
        print('There is no path to {}'.format(corner))
    else:
        print('The preferred path to {} is:'.format(corner))
        print('  ', path)
