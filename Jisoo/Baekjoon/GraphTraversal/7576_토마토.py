from collections import deque
queue = deque([])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
count = 0

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

while queue:
    y, x = queue.popleft()

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if (0<=ny<n) and (0<=nx<m):
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny, nx])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)

    count = max(count, max(graph[i]))

print(count - 1)