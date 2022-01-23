# 백준 7576 토마토

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = []
tomato = []
for i in range(n):
    box.append(list(map(int, input().split())))
    for j in range(m):
        if box[i][j] == 1:
            tomato.append((0, i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque(tomato)
while q:
    day, x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = 1
            q.append((day+1, nx, ny))

for i in range(n):
    if 0 in box[i]:
        print(-1)
        sys.exit(0)

print(day)