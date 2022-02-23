# 1374번 강의실 (Greedy) 
# https://www.acmicpc.net/problem/1374

import heapq

N = int(input())
timeTable = []
data = []
for _ in range(N):
    num, start, end = map(int, input().split())
    data.append((start, end))

data.sort()

timeTable.append(data[0][1])

for i in range(1, N):
    if data[i][0] >= timeTable[0]:
        heapq.heappop(timeTable)
    heapq.heappush(timeTable, data[i][1])

print(len(timeTable))