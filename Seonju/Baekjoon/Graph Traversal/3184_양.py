# 백준 3184 양

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    o = 0
    v = 0

    while q:
        x, y = q.popleft()

        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == '#':
                    continue
                elif graph[nx][ny] == 'v':
                    v += 1
                elif graph[nx][ny] == 'o':
                    o += 1
                q.append((nx, ny))
                visited[nx][ny] = 1

    return o, v


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(n):
        graph.append(list(input().rstrip()))

    # 방향벡터 (-, 상, 하, 좌, 우)
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    sheep, wolf = 0, 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] != '#':
                s, w = bfs(i, j)
                if s > w:
                    sheep += s
                else:
                    wolf += w

    print(sheep, wolf)
