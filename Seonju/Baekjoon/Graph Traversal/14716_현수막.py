# 백준 14716 현수막

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 2

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 2


n, m = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)
            cnt += 1

print(cnt)