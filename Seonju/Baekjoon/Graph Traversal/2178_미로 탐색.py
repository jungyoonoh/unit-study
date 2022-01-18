# 백준 2178 미로 탐색

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x-1, y-1)])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                q.append((nx, ny))
                maze[nx][ny] += maze[x][y]

    return maze[n-1][m-1]


if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = []

    for _ in range(n):
        maze.append(list(map(int, input().rstrip())))

    # 방향벡터 (상 하 좌 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(bfs(1, 1))
