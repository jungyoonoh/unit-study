#20220306
#백준(그래프 탐색) : 11725 트리의 부모 찾기
#https://www.acmicpc.net/problem/11725
#BFS
from collections import deque
n = int(input())

visited = [0 for _ in range(n+1)]
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b = map(int, input().split())
  # 연결 시키기
  tree[a].append(b)
  tree[b].append(a)
# print(tree)
q = deque()

#루트 1
q.append(1)
visited[1] = 1

while q:
  c = q.pop()

  for i in tree[c]:
    if visited[i] == 0:
      visited[i] = c  #부모 번호 저장
      q.append(i)

#노드 2번부터 출력
for i in range(2, n+1):
  print(visited[i])

