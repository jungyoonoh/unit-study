from collections import deque
queue = deque()

dy = [-1, 1, 0, 0, -1, 1, -1, 1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]
cnt = 0

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

while queue:
    y, x = queue.popleft()

    for d in range(8):
        ny = dy[d] + y
        nx = dx[d] + x

        if (0 <= ny < n) and (0 <= nx < m) and (graph[ny][nx] == 0):
            queue.append([ny, nx])
            graph[ny][nx] = graph[y][x] + 1
            cnt = max(cnt, graph[y][x] + 1)

print(cnt-1)

