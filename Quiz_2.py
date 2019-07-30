# Prompts the user for an integer N at least equal to 5,
# computes the largest number l >= 1 such that l consecutive prime numbers
# add up to a prime number at most equal to N,
# and outputs l and the larger such prime number.
#
# Extention: compare three different way to find the prime number and the computing speed
# Written by Xiaowen Huang

from math import sqrt
import sys
import time

# N % (2 -- sqrt(N) + 1)
def is_prime_1(N):
    if N < 2:
        return False
    else:
        for i in range(2, round(sqrt(N) + 1)):
            if N % i == 0:
                return False
    return True

# N is odd
# N % (2 -- sqrt(N) + 1)
def is_prime_2(N):
    if N < 2:
        return False
    elif N > 2 and N % 2 == 0:
        return False
    else:
        for i in range(2, round(sqrt(N) + 1)):
            if N % i == 0:
                return False
    return True

# N is the number next to the multiples of 6
def is_prime_3(N):
    if N < 2:
        return False
    elif N == 2 or N == 3 or N == 5:
        return True
    elif N % 6 != 1 and N % 6 != 5:
        return False
    else:
        for i in range(5, round(sqrt(N)+1), 6):
            if N % i == 0 or N % (i+2) == 0:
                return False
    return True

## Main function:
try:
    N = int(input('Enter an integer at least equal to 5: '))
    if N < 5:
        raise ValueError
except ValueError:
    print('Incorrent input, giving up.')
    sys.exit()

start = time.clock()
L = []
for i in range(2, N):
    if is_prime_1(i):
        L.append(i)
print(len(L), time.clock() - start)

start = time.clock()
L = []
for i in range(2, N):
    if is_prime_2(i):
        L.append(i)
print(len(L), time.clock() - start)

start = time.clock()
L = []
for i in range(2, N):
    if is_prime_3(i):
        L.append(i)
print(len(L), time.clock() - start)




