# 1504번 특정한 최단 경로 (dijkstra) 
# https://www.acmicpc.net/problem/1504

import sys, heapq
input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(s):
    hq = []
    xToOthers = [1e9] * (N+1) # dijkstra
    xToOthers[s] = 0
    heapq.heappush(hq, (0, s))
    
    while hq:
        weight, now = heapq.heappop(hq)

        if xToOthers[now] < weight: # 현재 가중치보다 이미 경로가 작다면
            continue
        
        for next, dist in graph[now]:
            cost = xToOthers[now] + dist 
            if cost < xToOthers[next]:
                xToOthers[next] = cost
                heapq.heappush(hq, (cost, next))
    
    return xToOthers

# 1 -> v1 -> v2 -> N 
# 1 -> v2 -> v1 -> N 둘중에 하나

dStart = dijkstra(1)
dV1 = dijkstra(v1)
dV2 = dijkstra(v2)

flag = True
if (dStart[v1] == 1e9 or dV1[v2] == 1e9 or dV2[N] == 1e9) and (dStart[v2] == 1e9 or dV2[v1] == 1e9 or dV1[N] == 1e9):
    flag = False

if flag:
    print(min(dStart[v1] + dV1[v2] + dV2[N], dStart[v2] + dV2[v1] + dV1[N]))
else:
    print(-1)
