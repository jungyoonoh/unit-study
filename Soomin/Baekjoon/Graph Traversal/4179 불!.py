#20220313
#백준(그래프 탐색) : 4179 불!
#https://www.acmicpc.net/problem/4179

from collections import deque

r, c = map(int,input().split())

maze = []

for _ in range(r):
  maze.append(list(input()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[0] * c for _ in range(r)]

for i in range(r):
  for j in range(c):    
    if maze[i][j] == 'J':
      q = deque([('J', i, j)])
      visited[i][j] = 1

for i in range(r):
  for j in range(c):    
    if maze[i][j] == 'F':
      q.append(('F', i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
  key, x, y = q.popleft()

  # 지훈이 탈출
  # 지훈이가 불을 안 만났고, 해당 범위일 때
  if key == 'J' and maze[x][y] != 'F' and (x == 0 or y == 0 or x == r-1 or y == c-1):
    print(visited[x][y])
    exit(0)

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] != '#':
      # 지훈
      if key == 'J' and visited[nx][ny] == 0 and maze[nx][ny] == '.':
        maze[nx][ny] = 'J'
        q.append(('J',nx,ny))
        visited[nx][ny] = visited[x][y] + 1
        
      # 불 
      elif key == 'F' and maze[nx][ny] != 'F':
        maze[nx][ny] = 'F'
        q.append(('F',nx,ny))
        
print('IMPOSSIBLE')