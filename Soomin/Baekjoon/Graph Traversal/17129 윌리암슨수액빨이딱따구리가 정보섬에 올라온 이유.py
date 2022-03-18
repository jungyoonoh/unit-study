#20220313
#백준(그래프 탐색) : 17129 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유
#https://www.acmicpc.net/problem/17129

from collections import deque

n, m = map(int,input().split())

a = []

for _ in range(n):
  aa = list(map(str,input()))
  a.append(list(map(int,aa)))
  
visited = [[0]*m for _ in range(n)]  

q = deque()
for i in range(n):
  for j in range(m):
    if a[i][j] == 2:
      q.append((i,j))
      visited[i][j] = 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


while q:
  x, y = q.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
      if a[nx][ny] == 0:

        q.append((nx,ny))
        visited[nx][ny] = visited[x][y] + 1
      
      elif a[nx][ny] == 3 or a[nx][ny] == 4 or a[nx][ny] == 5:
        print("TAK")
        print(visited[x][y])

        exit(0)
    
print("NIE")