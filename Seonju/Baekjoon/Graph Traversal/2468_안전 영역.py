# 백준 2468 안전 영역

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, height):
    q = deque([(x, y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > height and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))

    return 1


n = int(input())
graph = []
maxHeight = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    maxHeight = max(maxHeight, max(graph[i]))

maxCnt = 0
for k in range(maxHeight+1):
    cnt = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                cnt += bfs(i, j, k)
    maxCnt = max(maxCnt, cnt)

print(maxCnt)