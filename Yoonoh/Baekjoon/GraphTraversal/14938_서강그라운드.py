# 14938번 서강그라운드 (dijkstra) 
# https://www.acmicpc.net/problem/14938

import heapq

n, m, r = map(int, input().split()) # m 이내에 있는 아이템들
item = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
maxVal = 0
for i in range(r):
    start, end, length = map(int, input().split())
    graph[start].append((end, length))
    graph[end].append((start, length)) 
    
for start in range(1, n+1):
    hq = []
    distance = [1e9 for _ in range(n+1)]
    distance[start] = 0
    heapq.heappush(hq, (0, start))
    
    while hq:
        nowWeight, node = heapq.heappop(hq)
        
        if distance[node] < nowWeight:
            continue
        
        for next in graph[node]:
            cost = next[1] + distance[node]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(hq, (cost, next[0])) # next[0]로 가는데 걸리는 가중치비용
    
    temp = 0
    for i in range(1, n+1):
        if distance[i] <= m:
            temp += item[i]
    
    maxVal = max(temp, maxVal)

print(maxVal)