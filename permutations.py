"""
Input a list and generate all the permutations with 2 methods:

Firstly, using the normal recursion
Secondly, using DFS

Written by Xiaowen Huang
"""


raw = input('Please input a list: ').split()
L = [int(i) for i in raw]


def perm(n,begin,end):
    if begin >= end:
        print(n)

    else:
        i=begin
        for num in range(begin, end):
            n[num], n[i] = n[i], n[num]
            perm(n, begin+1, end)
            n[num], n[i] = n[i], n[num]


def dfs(position, L):
    visit = [True] * len(L)
    temp = [0] * len(L)

    def dfs_finding(position):
        if position == len(L):
            print(temp)
        else:
            for i in range(0, len(L)):
                if visit[i]:
                    temp[position] = L[i]
                    visit[i] = False
                    dfs_finding(position+1)
                    visit[i] = True

    dfs_finding(position)


print('Permutations generated with Recursion: ')
perm(L, 0, len(L))
print('Permutations generated with DFS: ')
dfs(0, L)