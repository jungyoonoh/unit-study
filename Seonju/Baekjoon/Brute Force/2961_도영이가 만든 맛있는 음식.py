# 백준 2961 도영이가 만든 맛있는 음식

import sys, itertools
input = sys.stdin.readline

n = int(input())
sour = []
bitter = []
for _ in range(n):
    a, b = map(int, input().split())
    sour.append(a)
    bitter.append(b)

diff = float('inf')

for i in range(1, n+1):
    lst = list(itertools.combinations(list(range(n)), i))

    for food in lst:
        s = 1
        b = 0

        for j in range(i):
            s *= sour[food[j]]
            b += bitter[food[j]]
        if abs(s - b) < diff:
            diff = abs(s - b)

print(diff)
