# 백준 2667 단지번호붙이기

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    cnt = 1

    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and town[nx][ny] == 1:
                town[nx][ny] += 1
                q.append((nx, ny))
                cnt += 1

    count.append(cnt)


if __name__ == '__main__':
    n = int(input())
    town = []

    for _ in range(n):
        town.append(list(map(int, input().rstrip())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    count = []

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and town[i][j] == 1:
                bfs(i, j)

    count.sort()
    print(len(count), *count, sep='\n')
