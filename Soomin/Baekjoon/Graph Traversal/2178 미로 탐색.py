#20220308
#백준(그래프 탐색) : 2178 미로 탐색
#https://www.acmicpc.net/problem/2178

from collections import deque


n, m = map(int, input().split())
maze = []
for _ in range(n):
  maze.append(list(map(int,list(input()))))

# print(maze)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[0] * m for _ in range(n)]
q = deque([(0, 0)])

visited[0][0] = 1

while q:
  a, b = q.popleft()

  if a == n-1 and b == m-1:
    print(visited[a][b])
    exit(0)

  for d in range(4):
    nx = a + dx[d]
    ny = b + dy[d]

    if 0 <= nx < n and 0 <= ny < m:
      if maze[nx][ny] == 1 and visited[nx][ny] == 0:
        visited[nx][ny] = visited[a][b] + 1
        q.append((nx,ny))

# print(maze[n-1][m-1])
  
      
  
  






