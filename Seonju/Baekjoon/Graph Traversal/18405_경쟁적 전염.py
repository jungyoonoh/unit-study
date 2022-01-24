# 백준 18405 경쟁적 전염

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

lab = []
virus = []

for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(n):
        if lab[i][j]:
            virus.append((lab[i][j], i, j, 0))
virus.sort()

s, a, b = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque(virus)
while q:
    val, x, y, sec = q.popleft()
    if sec == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not lab[nx][ny]:
            lab[nx][ny] = val
            q.append((val, nx, ny, sec + 1))

print(lab[a - 1][b - 1])