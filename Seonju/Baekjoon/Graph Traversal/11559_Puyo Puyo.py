# 백준 11559 Puyo Puyo

import sys
from collections import deque
input = sys.stdin.readline


def check_four(x, y):
    q = deque([(x, y)])
    now = graph[x][y]
    pos = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and graph[nx][ny] == now and not visited[nx][ny]:
                pos.append((nx, ny))
                q.append((nx, ny))
                visited[nx][ny] = 1

    if len(pos) >= 4:
        pos.sort(key=lambda x: (-x[1], x[0]))
        for i, j in pos:
            graph[i][j] = '_'
            bombList.append((i, j))


graph = [list(input().rstrip()) for i in range(12)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0

while True:
    visited = [[0] * 6 for _ in range(12)]
    bombList = []

    # 뿌요 4개 이상 모여있는 곳 있는지 체크해서 터뜨리기
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and graph[i][j] != '_' and not visited[i][j]:
                check_four(i, j)

    if len(bombList) == 0:
        break

    # 뿌요 내리기
    for bomb in bombList:
        x, y = bomb[0], bomb[1]
        for i in range(x, 0, -1):
            graph[i][y] = graph[i-1][y]
        graph[0][y] = '.'

    time += 1

print(time)
