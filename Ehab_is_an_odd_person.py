"""
Input n, n digital read,
for all the odd number obtained by adding the exchange position,
the output processing sequence lexicographically smallest

TRICK WAY:
If this list contains some odd elements and some even elements,
which means all the elements can be any positions.
Therefore, we just need to sort the list.

If this list only has odd or even, we output the original list.

"""

def find(l):
    odd = []
    even = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if even == [] or odd == []:
        return l
    else:
        return sorted(l)

raw = input('Please input a list: ').split()
L = [int(i) for i in raw]
print('The output list: \n', find(L))