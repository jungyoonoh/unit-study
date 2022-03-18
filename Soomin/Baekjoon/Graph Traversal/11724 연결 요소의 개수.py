#20220314
#백준(그래프 탐색) : 11724 연결 요소의 개수
#https://www.acmicpc.net/problem/11724

def dfs(v):
  visited[v] = 1
  for i in link[v]:
    if visited[i] == 0:
      dfs(i)

n, m = map(int,input().split())

link = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for i in range(m):
  a, b = map(int,input().split())
  link[a].append(b)
  link[b].append(a)

# print(link)

for j in range(1, n+1):
  if visited[j] == 0:
    dfs(j)
    count += 1

print(count)

