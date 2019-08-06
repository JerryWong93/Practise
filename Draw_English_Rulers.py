"""
Input two integers: one for number of Rulers, the other for the maximum length of rulers
Case1: Input: 1 4
        ---- 0
        -
        --
        -
        ---
        -
        --
        -
        ---- 1
Case2: Input 2 3
        --- 0
        -
        --
        -
        --- 1
        -
        --
        -
        --- 2
"""

import sys


def draw_line(length, labal = ''):
    for _ in range(length):
        print('-', end='')
    if labal != '':
        print(' ' + str(labal), end='\n')
    else:
        print()


def draw_internal(length):
    if length > 0:
        draw_internal(length-1)
        draw_line(length)
        draw_internal(length-1)


try:
    num, max_length = input('Please input two integers for number and length: ').split()
    num, max_length = int(num), int(max_length)
    if num < 1 or max_length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up!!')
    sys.exit()

draw_line(max_length, 0)
for i in range(1, num+1):
    draw_internal(max_length-1)
    draw_line(max_length, i)
