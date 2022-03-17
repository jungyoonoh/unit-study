#20220317
#백준(그래프 탐색) : 5567 결혼식
#https://www.acmicpc.net/problem/5567

n = int(input())
m = int(input())

f = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())

  f[b].append(a)
  f[a].append(b)

# print(f)
visited = [0 for _ in range(n+1)]

for i in f[1]:
  visited[i] = 1
  for j in f[i]:
    visited[j] = 1
visited[1] = 0
print(visited.count(1))