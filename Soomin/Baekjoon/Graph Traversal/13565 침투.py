#20220319
#백준(그래프 탐색) : 13565 침투
#https://www.acmicpc.net/problem/13565

from collections import deque

m, n = map(int,input().split())

f = []

for _ in range(m):
  f.append(list(map(int,list(map(str,input())))))
# print(f)
visited = [[0] * n for _ in range(m)]
q = deque()
for i in range(n):
  if f[0][i] == 0:
    q.append((0,i))
    visited[0][i] = 1


dx = [0,0,1,-1]
dy = [-1,1,0,0]

while q:
  a, b = q.popleft()
  # print(a,b)
  if a == m-1:
    print("YES")
    # print(visited)
    exit(0)
  # visited[a][b] = 1

  for i in range(4):
    nx = a + dx[i]
    ny = b + dy[i]

    if 0 <= nx < m and 0 <= ny < n:
      if visited[nx][ny] == 0 and f[nx][ny] == 0:
        visited[nx][ny] = 1
        q.append((nx,ny))


print("NO")

  
