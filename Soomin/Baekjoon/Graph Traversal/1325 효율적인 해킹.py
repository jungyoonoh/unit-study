#20220309
#백준(그래프 탐색) : 1325 효율적인 해킹
#https://www.acmicpc.net/problem/1325

from collections import deque
n, m = map(int,input().split())

com = [[] for _ in range(n+1)]


for _ in range(m):
  a, b = map(int,input().split())
  # com[a].append(b)
  com[b].append(a)

ans = [0] * (n+1)

for j in range(1,n+1):
  q = deque()
  visited = [0 for _ in range(n+1)] #매번 초기화 해주는 것이 포인트
  count = 1
  
  q.append(j)
  visited[j] = 1
  # print(com)
  
  while q:
    c = q.pop()
    # print(c)
  
    for i in com[c]:
      if visited[i] == 0:
        count += 1
        visited[i] = 1
        q.append(i)
  ans[j] = count
# print(ans)

max_num = max(ans)

for i in range(n+1):
  if ans[i] == max_num:
    print(i,end = ' ')
      