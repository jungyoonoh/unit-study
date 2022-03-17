# 백준 18243 Small World Network

import sys, heapq
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start):
    q = [(0, start)]
    distance = [INF] * n
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    distance[start] = 0
    return distance


n, k = map(int, input().split())
graph = [[] * n for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1].append((b-1, 1))
    graph[b-1].append((a-1, 1))

result = []
for i in range(n):
    result.append(max(dijkstra(i)))

print('Big World!' if max(result) > 6 else 'Small World!')
