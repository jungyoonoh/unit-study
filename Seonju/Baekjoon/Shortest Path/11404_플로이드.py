# 백준 11404 플로이드

import sys
input = sys.stdin.readline

n = int(input())

city = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if not city[a-1][b-1] or city[a-1][b-1] > c:
        city[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if city[i][k] and city[k][j]:
                cost = city[i][k] + city[k][j]
                if not city[i][j] or city[i][j] > cost:
                    city[i][j] = cost

for i in range(n):
    print(*city[i], sep=' ')
