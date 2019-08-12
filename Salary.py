"""
Interview questions:
发工资：
1。每人至少100
2。论资排辈：每人进入公司的工龄是公开的，如果员工A比相邻的员工B早进公司，那A至少比B拿多100
Input:
number of staff
The time of every staff
Output:
The pay of every staff
"""

number = int(input())
raw = input().split()
L = [int(i) for i in raw]
pay = [0] * len(L)

sort_L = sorted(list(set(L)))
for m in range(len(sort_L)):
    index = []
    index = [i for i, j in enumerate(L) if j == sort_L[m]]
    for n in index:
        if n == 0:
            if L[n+1] > L[n]:
                pay[n] = 100
            elif L[n+1] == L[n] and pay[n+1] != 0:
                pay[n] = pay[n+1]
            else:
                pay[n] = pay[n+1]+100
        elif n == number-1:
            if L[n-1] > L[n]:
                pay[n] = 100
            elif L[n-1] == L[n] and pay[n-1] != 0:
                pay[n] = pay[n-1]
            else:
                pay[n] = pay[n-1]+100

        elif L[n-1] > L[n] and L[n+1] > L[n]:
            pay[n] = 100
        elif L[n-1] == L[n] and pay[n-1] != 0:
            pay[n] = pay[n-1]
        elif L[n+1] == L[n] and pay[n+1] != 0:
            pay[n] = pay[n+1]
        else:
            pay[n] = max(pay[n-1], pay[n+1]) + 100

print(pay)
