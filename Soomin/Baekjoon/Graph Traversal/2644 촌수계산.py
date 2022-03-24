#20220318
#백준(그래프 탐색) : 2644 촌수계산
#https://www.acmicpc.net/problem/2644

from collections import deque

n = int(input())

a, b = map(int,input().split())
m = int(input())
p = [[] for _ in range(n+1)]

for i in range(m):
  x, y = map(int,input().split())
  p[x].append(y)
  p[y].append(x)

# print(p)
visited = [0] * (n+1) 
q = deque()
q.append(a)

while q:
  pa = q.popleft()

  for i in p[pa]:
    if visited[i] == 0:
      visited[i] = visited[pa] + 1
      q.append(i)

# print(visited)

if visited[b] > 0:
  print(visited[b])
else:
  print(-1)