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
# Written by Xiaowen Huang


import sys
from random import seed, choice
from collections import deque


def display_grid():
    for i in range(dim):
        print('    ', end='')
        for j in range(dim):
            print(' ', grid[i][j], end='')
        print()
    print()


def preferred_paths_to_corners():
    next_dir = {'SW': [(1, -1), (0, -1), (1, 0)], 'SE': [(1, 1), (0, 1), (1, 0)], 'NE': [(-1, 1), (0, 1), (-1, 0)],
                'NW': [(-1, -1), (0, -1), (-1, 0)]}
    point = {}
    paths = {}
    for i in range(dim):
        for j in range(dim):
            a, b, c = next_dir[grid[i][j]]
            point[(i, j)] = []
            if 0 <= i + a[0] < dim and 0 <= j + a[1] < dim:
                point[(i, j)].append((i + a[0], j + a[1]))
            if 0 <= i + b[0] < dim and 0 <= j + b[1] < dim:
                point[(i, j)].append((i + b[0], j + b[1]))
            if 0 <= i + c[0] < dim and 0 <= j + c[1] < dim:
                point[(i, j)].append((i + c[0], j + c[1]))
    for x in corners:
        pass_path = []
        tree = (3, 3), point
        queue = deque([[tree[0]]])
        while queue:
            path = queue.pop()
            if path[-1] == x:
                paths[(x[1], x[0])] = path
                break
            if path[-1] in tree[1]:
                for c in tree[1][path[-1]]:
                    if c not in pass_path and (c not in corners or c == x):
                        #                        print(c)
                        queue.appendleft(path + [c])
                        pass_path.append(c)
    #                        print(pass_path)
    print(paths)
    for m in paths:
        for n in range(len(paths[m])):
            temp = (paths[m][n][1], paths[m][n][0])
            paths[m][n] = temp
    return paths

    # replace pass above with your code (aim for around 21 lines of code)


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
