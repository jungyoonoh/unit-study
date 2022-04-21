import sys
sys.setrecursionlimit(10000)
 #   상 하 좌 우 상좌 상우 하좌 하우
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

def DFS(y, x, hh, ww):
    graph[y][x] = 0

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]

        if (0<=ny<hh) and (0<=nx<ww):
            if graph[ny][nx] == 1:
                DFS(ny, nx, hh, ww)

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        exit(0)

    graph = [list(map(int, input().split())) for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                DFS(i, j, h, w)
                count = count + 1

    print(count)