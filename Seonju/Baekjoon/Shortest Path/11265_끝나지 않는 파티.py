# 백준 11265 끝나지 않는 파티

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for _ in range(m):
    a, b, time = map(int, input().split())
    if graph[a-1][b-1] <= time:
        print('Enjoy other party')
    else:
        print('Stay here')