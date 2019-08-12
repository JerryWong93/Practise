"""
 Quick sorting:
 Worst case: O(n**2)
 Average case: O(n logn)
"""
from copy import deepcopy as dc


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l


def quick_sort(l, left, right):
    if left >= right:
        return
    # the left element will be the pivot
    pivot = l[left]
    i, j = left, right
    while i < j:
        while l[j] >= pivot and i < j:
            j -= 1
        while l[i] <= pivot and i < j:
            i += 1
        # exchange
        temp = l[j]
        l[j] = l[i]
        l[i] = temp
    # pivot return to the right position
    if i == j:
        l[left] = l[i]
        l[i] = pivot
        quick_sort(l, left, i-1)
        quick_sort(l, i+1, right)
    return l


# merge sort
def merge(lst, l, mid, r):
    left = lst[l:mid+1]
    right = lst[mid+1:r+1]
    while left and right:
        if left[0] < right[0]:
            lst[l] = left.pop(0)
        else:
            lst[l] = right.pop(0)
        l += 1
    tail = left if left else right
    for n in tail:
        lst[l] = n
        l += 1
    return lst

def merge_sort(lst, l, r):
    if l < r:
        mid = (l+r) // 2
        merge_sort(lst, l, mid)
        merge_sort(lst, mid+1, r)
        merge(lst, l, mid, r)
        return lst


raw = input('Please input a list: ').split()
L = [int(i) for i in raw]
print('Bubble sorting: {}'.format(bubble_sort(dc(L))))
print('Quick sorting: {}'.format(quick_sort(dc(L), 0, len(L)-1)))
print('Merge sorting: {}'.format(merge_sort(dc(L), 0, len(L)-1)))