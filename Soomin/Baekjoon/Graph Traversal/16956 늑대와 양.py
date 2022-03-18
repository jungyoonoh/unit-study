#20220311
#백준(그래프 탐색) : 16956 늑대와 양
#https://www.acmicpc.net/problem/16956

from collections import deque
r, c = map(int,input().split())
m = []

for _ in range(r):
  m.append(list(input()))

dx = [0,0,1,-1]
dy = [-1,1,0,0]
q = deque()

for i in range(r):
  for j in range(c):
    if m[i][j] == 'S':
      q.append((i,j))

check = False

while q:
  a, b = q.popleft()
  

  for i in range(4):
    nx = a + dx[i]
    ny = b + dy[i]
    # q.append((nx,ny))

    if 0 <= nx < r and 0 <= ny < c:
      if m[nx][ny] == 'W':
        print(0)
        exit(0)
      elif m[nx][ny] == '.':
        m[nx][ny] = 'D'
        check = True

if check:
  # print(0)
  print(1)
  for k in range(r):
    print(''.join(m[k]))
else:
  print(0)