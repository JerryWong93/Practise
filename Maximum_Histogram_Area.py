"""
Source: https://www.youtube.com/watch?v=ZmnqCZp9bBs
1. Add the stack if current value is equal or bigger than top of stack
2. Otherwise keep removing from the stack till a number which is smaller or equal
   than current
3. Calculate area every time when remove:
    if (steak is empty):
        area = input[top] * i
    else:
        area = input[top] * (i - steak.top -1)
    ======= ps. steak.top is the top of steak after pop
"""

import sys

raw = input('Please input a non-negative list: ').split()
L = [int(i) for i in raw]
stack = []
area = 0
max_area = 0
i = 0

while i <= len(L)-1:
    if len(stack) == 0 or L[i] >= L[stack[-1]]:
        stack.append(i)
        i += 1
    else:
        top = stack.pop()
        if (len(stack) == 0):
            area = L[top] * i
        else:
            area = L[top] * (i -stack[-1] -1)
        if area > max_area:
            max_area = area

while len(stack) != 0:
    top = stack.pop()
    if (len(stack) == 0):
        area = L[top] * i
    else:
        area = L[top] * (i -stack[-1] -1)
    if area > max_area:
        max_area = area

print(max_area)



