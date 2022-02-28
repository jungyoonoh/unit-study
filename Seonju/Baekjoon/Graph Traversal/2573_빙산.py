# 백준 2573 빙산

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:  # 바다면
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:  # 아직 방문하지 않은 빙산이면
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0:  # (x, y) 주위에 바다가 있다면
            seaList.append((x, y, sea))

    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)

    return 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ice = []  # 빙산이 있는 위치를 인덱스로 저장
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

year = 0

while ice:
    # 1년치 빙산 녹이기
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0:
            delList.append((i, j))

    if group > 1:
        print(year)
        break

    ice = sorted(list(set(ice) - set(delList)))  # 다 녹은 빙산은 제거
    year += 1

if group < 2:
    print(0)
