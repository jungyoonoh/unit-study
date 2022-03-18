#20220316
#백준(그래프 탐색) : 17086 아기 상어 2
#https://www.acmicpc.net/problem/17086

from collections import deque

n, m = map(int,input().split())

p = []

for _ in range(n):
  p.append(list(map(int,input().split())))

# print(p)

visited = [[0] * m for _ in range(n)]

dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,-1,1,-1,1]

q = deque()

for i in range(n):
  for j in range(m):
    if p[i][j] == 1:
      q.append((i,j))
      # visited[i][j] = 1
max1 = 0
while q:
  a, b = q.popleft()

  for i in range(8):
    nx = a + dx[i]
    ny = b + dy[i]

    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
      if p[nx][ny] == 0:
        visited[nx][ny] = visited[a][b] + 1
        q.append((nx,ny))

      if visited[nx][ny] > max1:
        max1 = visited[nx][ny]

print(max1)
# print(visited)