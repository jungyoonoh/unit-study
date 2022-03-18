# 백준 2636 치즈

import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
cheeze = []
cnt = 0
for i in range(n):
    cheeze.append(list(map(int, input().split())))
    cnt += cheeze[i].count(1)  # 전체 치즈 갯수 카운팅
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_air(x, y):  # 공기 배열 air 초기화 (공기인 곳은 값을 1로)
    q = deque([(x, y)])
    air = [[0] * m for _ in range(n)]
    air[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not cheeze[nx][ny] and not air[nx][ny]:
                air[nx][ny] = 1
                q.append((nx, ny))
    return air


def melt_cheeze(x, y):  # 공기와 맞닿은 치즈 녹이기
    q = deque([(x, y)])
    melt_cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if air[nx][ny] and cheeze[x][y]:
                    cheeze[x][y] = 0
                    air[x][y] = 1
                    melt_cnt += 1
                elif cheeze[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    return melt_cnt


time = 1
while True:
    now_melt = 0
    visited = [[0] * m for _ in range(n)]

    air = check_air(0, 0)

    for i in range(n):
        for j in range(m):
            if cheeze[i][j] and not visited[i][j]:
                now_melt += melt_cheeze(i, j)
    cnt -= now_melt

    if cnt == 0:
        print(time, now_melt, sep='\n')
        break

    time += 1
