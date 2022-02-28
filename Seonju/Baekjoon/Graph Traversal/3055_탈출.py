# 백준 3055 탈출

import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = -1

for i in range(n):
    graph.append(list(input().rstrip()))
    if 'S' in graph[i]:
        q = deque([(0, i, graph[i].index('S'))])

for i in range(n):
    for j in range(m):
        if graph[i][j] == '*':
            q.append((-1, i, j))

while q:
    time, x, y = q.popleft()

    if time >= 0 and graph[x][y] == '*':
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:

            # 물 먼저 퍼뜨리기
            if time == -1 and (graph[nx][ny] != 'X' and graph[nx][ny] != '*' and graph[nx][ny] != 'D'):
                graph[nx][ny] = '*'
                q.append((-1, nx, ny))

            # 고슴도치 이동하기
            elif time >= 0:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '_'
                    q.append((time + 1, nx, ny))
                if graph[nx][ny] == 'D':
                    print(time + 1)
                    sys.exit(0)

print('KAKTUS')