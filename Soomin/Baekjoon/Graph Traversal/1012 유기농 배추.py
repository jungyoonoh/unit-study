#20220312
#백준(그래프 탐색) : 1012 유기농 배추
#https://www.acmicpc.net/problem/1012
#BFS

from collections import deque

t = int(input())

ans = []
def bfs(x,y):
  q = deque()

  q.append((x,y))
  go[x][y] = 0
  dx = [0,0,-1,1]
  dy = [1,-1,0,0]
  
  while q:
    c, d = q.popleft()

    for i in range(4):
      nx = c + dx[i]
      ny = d + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if go[nx][ny] == 1:
          q.append((nx,ny))
          go[nx][ny] = 0
          

while t != 0:
  m, n, k = map(int,input().split())

  go = [[0]*n for _ in range(m)]
  # print(go)
  count = 0
  for _ in range(k):
    a, b = map(int,input().split())
    go[a][b] = 1

  for i in range(m):
    for j in range(n):
      if go[i][j] == 1:
        bfs(i,j)
        count += 1
  print(count)
  t -= 1