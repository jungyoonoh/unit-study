# 백준 16174 점프왕 쩰리 (Large)

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        if (x, y) == (n - 1, n - 1):
            return 1
        for i in range(2):
            nx = x + dx[i] * graph[x][y]
            ny = y + dy[i] * graph[x][y]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
    return 0


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [0, 1]
dy = [1, 0]
print("HaruHaru" if bfs(0, 0) else "Hing")