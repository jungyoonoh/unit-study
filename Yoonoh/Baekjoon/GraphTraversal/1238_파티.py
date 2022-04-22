# 1238번 파티 (dijkstra) 
# https://www.acmicpc.net/problem/1238

# 1. X 마을에서 나머지로 모이는데 걸리는 시간 -> 다익스트라

import heapq, sys
input = sys.stdin.readline
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)] 

for i in range(M):
    start, end, T = map(int, input().split())
    graph[start].append((end, T)) # 단방향

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

distance = [[], ]
for i in range(1, N+1):
    distance.append(dijkstra(i))

maxVal = 0
for i in range(1, N+1):
    maxVal = max(maxVal, distance[i][X] + distance[X][i])

print(maxVal)