# 19598번 최소 회의실 개수 (Greedy) 
# https://www.acmicpc.net/problem/19598

import heapq

N = int(input())
timeTable = []
for i in range(N):
    start, end = map(int, input().split())
    timeTable.append((start, end))

timeTable.sort()

hq = []
heapq.heappush(hq, timeTable[0][1])

for i in range(1, N):
    if timeTable[i][0] >= hq[0]:
        heapq.heappop(hq)
    heapq.heappush(hq, timeTable[i][1])
    
print(len(hq))