# 백준 1956 운동

import sys
input = sys.stdin.readline
INF = float('inf')

v, e = map(int, input().split())
graph = [[INF] * v for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c

cycle = INF
for k in range(v):
    for i in range(v):
        for j in range(v):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
            if i == j and cycle > graph[i][j]:
                cycle = graph[i][j]

print(cycle if cycle != INF else -1)