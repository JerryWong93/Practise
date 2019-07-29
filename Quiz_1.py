# Generates a list L of random non-negative integers at most equal to some value
# input by the user, and of length also input by the user, and outputs a list
# consisting of the longest streak of consecutive occurrences of the same value in L,
# possibly looping around (as if the list was a ring). In the case multiple value
# have the longest streak of consecutive occurrences in L, then the smallest value is chosen.

# Written by Xiaowen Huang

import sys
from random import seed, randint
try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers:').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
print('\nThe generated list is: ')
print(' ', L)
R = L

results = []
times = []

number = R[0]
count = 1
for i in range(1, len(R)+1):
    if i == len(R):
        results.append(number)
        times.append(count)
    elif R[i] == number:
        count += 1
    else:
        results.append(number)
        times.append(count)
        number = R[i]
        count = 1

if results[0] == results[-1]:
    times[0] = times[0] + times[-1]

max_index = [i for i, v in enumerate(times) if v == max(times)]
all_numbers = [results[num] for num in max_index]
out = [min(all_numbers)] * max(times)
print('\nThe longest steak of the same value is: ')
print(' ', out)
# print(results)
# print(times)
