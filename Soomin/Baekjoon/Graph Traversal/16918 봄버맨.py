#20220310
#백준(그래프 탐색) : 16918 봄버맨
#https://www.acmicpc.net/problem/16918

from collections import deque
r, c, n = map(int,input().split())
rc = []

for _ in range(r):
  rc.append(list(input()))

# print(rc)


time = 1
# bomb = [[-1] * c for _ in range(r)]

#세가지 케이스를 나눠서 만들어줘야 한다
def first():
  for i in range(r):
    for j in range(c):
      if rc[i][j] == 'O':
        # bfs(time,i,j)
        q.append((i,j))
    
def second():
  for a in range(r):
    for b in range(c):
      if rc[a][b] == '.':
        rc[a][b] = 'O'
        # bomb[a][b] = t

def third():
  dx = [0,0,1,-1]
  dy = [1,-1,0,0]
  while q:
    x, y = q.popleft()
    rc[x][y] = '.'
    # print(x,y)

    for a in range(4):
      nx = x + dx[a]
      ny = y + dy[a] 
      if 0<= nx < r and 0 <= ny < c:
        if rc[nx][ny] == 'O':
          # print('hi')
          rc[nx][ny] = '.'

n -= 1

while n:
  q = deque()

  first()

  second()

  n -= 1

  if n == 0:
    break
  
  third()
  n -= 1
  
# print(rc)
for p in rc:
  print(''.join(p))