#20220307
#백준(그래프 탐색) : 1260 DFS와 BFS
#https://www.acmicpc.net/problem/1260

from collections import deque

def dfs(v):
  vb[v] = 1
  print(v, end =' ')
  for i in bf[v]:
    if vb[i] == 0:
      dfs(i)

def bfs(v):
 
  q.append(v)
  vb[v] = 1
  
  while q:
    bp = q.popleft()
    print(bp, end = ' ')
  
    for i in bf[bp]:
      if vb[i] == 0:
        vb[i] = 1
        q.append(i)
  
  # print(vb)
        
n, m, v = map(int,input().split())

bf = [[] for _ in range(n+1)]
vb = [0 for _ in range(n+1)]

for _ in range(m):
  a, b = map(int,input().split())
  bf[a].append(b)
  bf[b].append(a)
# print(bf)

#정렬
for i in range(1,n+1):
  bf[i].sort()

  
q = deque()



dfs(v)

print()
vb = [0 for _ in range(n+1)]

bfs(v)