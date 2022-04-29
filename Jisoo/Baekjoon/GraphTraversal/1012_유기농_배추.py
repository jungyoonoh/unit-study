import sys
sys.setrecursionlimit(10000)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

t = int(input())

def DFS(yy, xx, nn, mm):
    graph[yy][xx] = 0

    for d in range(4):
        ny = yy + dy[d]
        nx = xx + dx[d]

        if (0<=ny<nn) and (0<=nx<mm):
            if graph[ny][nx]:
                DFS(ny, nx, nn, mm)


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                DFS(i, j, n, m)
                count = count+1

    print(count)
