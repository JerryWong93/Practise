# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out".
#
# Written by Xiaowen Huang

from random import seed, randrange
import sys

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end='') if grid[i][j] else print(' 0', end='')
        print()
    print()

def display(g):
    for i in range(dim+2):
        print('    ', end = '')
        for j in range(dim+2):
            print(g[i][j], end=' ')
        print()
    print()

# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s that make it with 2.
# We "colour" the second shape we find by replacing all the 1s that make it with 3.
# etc.

# recursion for finding 1s
def finding(i,j,k,g):
    g[i][j] = k
    if g[i-1][j] == 1:
        finding(i-1,j,k,g)
    if g[i+1][j] == 1:
        finding(i+1,j,k,g)
    if g[i][j-1] == 1:
        finding(i,j-1,k,g)
    if g[i][j+1] == 1:
        finding(i,j+1,k,g)
    return g

def color_shape(list_grid):
    k = 1
    for i in range(dim+2):
        for j in range(dim+2):
            if list_grid[i][j] == 1:
                k += 1
                list_grid = finding(i,j,k,list_grid)
    return spike(list_grid, k)

def spike(g, k):
    max_num = 0
    # display(g)
    for m in range(2, k+1):
        num = 0
        for i in range(1, dim+2):
            for j in range(1, dim+2):
                if g[i][j] == m and g[i-1][j] + g[i+1][j] + g[i][j-1] + g[i][j+1] == m:
                    num += 1
        if num > max_num:
            max_num = num
                # print((i,j))
    return max_num


dim = 10
try:
    for_seed, n = [int(i) for i in input('Enter two integers, the second one being strict positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) != 0 for _ in range(dim)]for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

list_grid = [[0 for _ in range(dim+2)]for _ in range(dim+2)]
for i in range(0,dim):
    for j in range(0,dim):
        if grid[i][j]:
            list_grid[i+1][j+1] = 1
        else:
            list_grid[i+1][j+1] = 0

n = color_shape(list_grid)
print(n)
print('The maximum number of spikes of some shape is equal to {}'.format(n))