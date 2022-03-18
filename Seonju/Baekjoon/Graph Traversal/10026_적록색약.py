# 백준 10026 적록색약

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    color = graph[x][y]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return 1


def traversal():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += bfs(i, j)
    print(cnt, end=" ")


n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
traversal()  # 적록색약이 아닌 사람

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
traversal()  # 적록색약인 사람
