# 25195번 Yes or yes (Graph) 
# https://www.acmicpc.net/problem/25195

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

gomSpot = [False] * (N+1)
graph = [[] for _ in range(N+1)]
endOfTravel = [True] * (N+1) # 더이상 갈 수 있는곳 X
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    endOfTravel[start] = False

S = int(input())
spot = list(map(int, input().split()))
for i in range(S):
    gomSpot[spot[i]] = True
    
isVisited = [False] * (N+1)

dq = deque()
dq.append(1)
isVisited[1] = True

flag = False
while dq:
    x = dq.popleft()
    if gomSpot[x]:
        continue
    
    if endOfTravel[x]:
        flag = True
        break
    
    for next in graph[x]:
        if not isVisited[next]:
            isVisited[next] = True
            dq.append(next)

print("Yes" if not flag else "yes")