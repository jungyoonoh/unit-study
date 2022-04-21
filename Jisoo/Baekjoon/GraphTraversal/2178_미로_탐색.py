from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
visited_count = [[0]*m for _ in range(n)]

y = x = 0

queue = deque()
queue.append((0, 0))

visited[0][0] = True
visited_count[0][0] = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while queue:
    y, x = queue.popleft()

    if n == y and m == x:
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if (0 <= ny < n) and (0 <= nx < m):
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append([ny, nx])
                visited_count[ny][nx] += visited_count[y][x] + 1

print(visited_count[n-1][m-1])