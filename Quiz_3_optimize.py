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
# This version is applying the classical algorithm Maximum histogram area

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

def size(list_grid, d):
    list_area = 0
    current_statement = copy.deepcopy(list_grid[0])
    for i in range(1, dim):
        for j in range(d):
            if list_grid[i][j] == 1:
                current_statement[j] = current_statement[j]+1
            else:
                current_statement[j] = 0
        if list_area < maximum_histogram_area(current_statement):
            list_area = maximum_histogram_area(current_statement)
    return list_area

def size_of_largest_parallelogram(list_grid):
    #rectagle
    g1 = copy.deepcopy(list_grid)
    s1 = size(g1, 10)

    #right
    g2 = copy.deepcopy(list_grid)
    for i in range(0, 10):
        for n in range(i):
            g2[i].insert(0, 0)
        for n in range(10 - i):
            g2[i].append(0)
    s2 = size(g2, 20)

    #left
    g3 = copy.deepcopy(list_grid)
    for i in range(0, 10):
        for n in range(10 - i):
            g3[i].insert(0, 0)
        for n in range(i):
            g3[i].append(0)
    s3 = size(g3, 20)

    max_value = max(s1,s2,s3)
    return max_value



def maximum_histogram_area(l):
    i = 0
    area = 0
    max_area = 0
    stack = []
    while i < len(l):
        if len(stack) == 0 or l[i] >= l[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if stack == []:
                if l[top] >= 2 and i >= 2:
                    area = l[top] * i
                else:
                    area = 0
            else:
                if l[top] >= 2 and i-stack[-1]-1 >= 2:
                    area = l[top] * (i-stack[-1]-1)
                else:
                    area = 0
            if max_area < area:
                max_area = area

    while len(stack) != 0:
        top = stack.pop()
        if stack == []:
            if l[top] >= 2 and i >= 2:
                area = l[top] * i
            else:
                area = 0
        else:
            if l[top] >= 2 and i - stack[-1] - 1 >= 2:
                area = l[top] * (i - stack[-1] - 1)
            else:
                area = 0
        if max_area < area:
            max_area = area

    return  max_area


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