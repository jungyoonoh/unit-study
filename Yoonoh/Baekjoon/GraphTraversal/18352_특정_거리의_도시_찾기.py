# 18352번 특정 거리의 도시 찾기 (Graph) 
# https://www.acmicpc.net/problem/18352

from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [0] * (N+1)
isVisited = [False] * (N+1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

dq = deque()
dq.append(X)
dist[X], isVisited[X] = 0, True 
ans = []
while dq: # 전체 도로가 100만개이므로
    now = dq.popleft()

    if dist[now] == K:
        ans.append(now)
        continue
    
    for next in graph[now]:
        if not isVisited[next]:
            isVisited[next] = True
            dist[next] = dist[now] + 1
            dq.append(next)

if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)