# 백준 18352 특정 거리의 도시 찾기

import sys, heapq
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m, k, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

dijkstra(start)

ans = []
for i in range(1, n+1):
    if distance[i] == k:
        ans.append(i)

if len(ans):
    print(*ans, sep='\n')
else:
    print(-1)