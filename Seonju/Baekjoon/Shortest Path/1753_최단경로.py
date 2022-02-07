# 백준 1753 최단경로

import sys, heapq
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start-1))
    distance[start-1] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v)]
distance = [INF] * v

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))

dijkstra(start)

for i in distance:
    print(i if i != INF else 'INF')