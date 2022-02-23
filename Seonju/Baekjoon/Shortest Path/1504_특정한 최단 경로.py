# 백준 1504 특정한 최단 경로

import sys, heapq
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start):
    distance = [INF for _ in range(n+1)]
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

    return distance


n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 1 - v1 - v2 - n
dist1 = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[n]

# 1 - v2 - v1 - n
dist2 = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[n]

ans = min(dist1, dist2)
print(ans if ans != INF else -1)