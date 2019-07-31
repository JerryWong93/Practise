# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111
#
# Written by Xiaowen Huang


from random import seed, randrange
import copy
import sys

dim = 10


def display_grid():
    for i in range(dim):
        print('    ', end='')
        for j in range(dim):
            print(' 1', end='') if grid[i][j] else print(' 0', end='')
        print()
    print()


def size_of_largest_parallelogram(list_grid):
    max_square = []

    def calculation(grid, dim):
        current_statement = copy.deepcopy(grid[0])
        size_group = [0]
        for i in range(1, 10):
            consecutive_list = []
            for j in range(0, dim):
                if grid[i][j] == 1:
                    current_statement[j] += 1
                else:
                    current_statement[j] = 0
            for i in range(0, dim):
                if current_statement[i] > 1:
                    consecutive_list.append(current_statement[i])
                    if i == dim - 1:
                        for i in range(0, len(consecutive_list)):
                            for n in range(i + 1, len(consecutive_list)):
                                temp = min(consecutive_list[i:n + 1]) * (n - i + 1)
                                size_group.append(temp)
                        consecutive_list = []
                else:
                    if len(consecutive_list) > 1:
                        for i in range(0, len(consecutive_list)):
                            for n in range(i + 1, len(consecutive_list)):
                                temp = min(consecutive_list[i:n + 1]) * (n - i + 1)
                                size_group.append(temp)
                        consecutive_list = []
                    else:
                        consecutive_list = []
        return max(size_group)

    grid = (())
    grid = copy.copy(list_grid)
    max_square.append(calculation(grid, 10))

    right_grid = (())
    right_grid = copy.deepcopy(list_grid)
    for i in range(0, 10):
        for n in range(i):
            right_grid[i].insert(0, 0)
        for n in range(10 - i):
            right_grid[i].append(0)
    max_square.append(calculation(right_grid, 20))

    left_grid = (())
    left_grid = copy.deepcopy(list_grid)
    for i in range(0, 10):
        for n in range(10 - i):
            left_grid[i].insert(0, 0)
        for n in range(i):
            left_grid[i].append(0)
    max_square.append(calculation(left_grid, 20))
    return max(max_square)


try:
    for_seed, n = [int(i) for i in
                   input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
list_grid = [[randrange(1) for _ in range(dim)] for _ in range(dim)]
for i in range(dim):
    for j in range(dim):
        if grid[i][j]:
            list_grid[i][j] = 1
        else:
            list_grid[i][j] = 0

size = size_of_largest_parallelogram(list_grid)
if size:
    print('The largest parallelogram with horizontal sides has a size of', size, end='.\n')
else:
    print('There is no parallelogram with horizontal sides.')


