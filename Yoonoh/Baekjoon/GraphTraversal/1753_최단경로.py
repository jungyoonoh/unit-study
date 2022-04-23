# 1753번 최단경로 (dijkstra) 
# https://www.acmicpc.net/problem/1753

from math import dist
import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
distance = [1e9] * (V+1)
distance[start] = 0
graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) 

hq = []
heapq.heappush(hq, (0, start))

while hq:
    nowWeight, node = heapq.heappop(hq) # node로 오는 특정 경로의 가중치의 합, start -> node 갱신된 distance 값 
    
    if distance[node] < nowWeight:  
        continue
    
    for next, d in graph[node]:
        cost = distance[node] + d
        if distance[next] > cost:
            distance[next] = cost
            heapq.heappush(hq, (cost, next))

for i in range(1, V+1):
    print("INF" if distance[i] == 1e9 else distance[i])