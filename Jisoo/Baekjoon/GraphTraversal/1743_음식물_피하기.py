from collections import deque
queue = deque([])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
n, m, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

def BFS(yy, xx):
    queue.append([yy, xx])
    count = 0

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if (0<=ny<n) and (0<=nx<m):
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 2
                    queue.append([ny, nx])
                    count = count + 1
    return count

count_max = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt = BFS(i, j)
            count_max = max(count_max, cnt)

print(count_max)