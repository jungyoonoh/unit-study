# 백준 14938 서강그라운드

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
graph = [[float('inf')] * n for _ in range(n)]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            elif graph[i][k] and graph[k][j]:
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

eat = 0
for i in range(n):
    tmp = 0
    for j in range(n):
        if graph[i][j] <= m:
            tmp += item[j]
    eat = max(eat, tmp)

print(eat)