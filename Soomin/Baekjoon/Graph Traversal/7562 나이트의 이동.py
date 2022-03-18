#20220315
#백준(그래프 탐색) : 7562 나이트의 이동
#https://www.acmicpc.net/problem/7562

from collections import deque

t = int(input())

for _ in range(t):
  l = int(input())

  sx, sy = map(int,input().split())
  ex, ey = map(int,input().split())

  visited = [[0] * l for _ in range(l)]



  dx = [-2, -2, 2, 2, -1, 1,-1, 1]
  dy = [-1, 1,-1, 1, -2, -2, 2, 2]

  q = deque()
  q.append((sx,sy))
  visited[sx][sy] = 1

  while q:
    x, y = q.popleft()
    
    if x == ex and y == ey:
      # print(visited[x][y]-1)
      break
      


    
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < l and 0 <= ny < l and visited[nx][ny]==0:
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx,ny))
  print(visited[ex][ey]-1)

  


  

