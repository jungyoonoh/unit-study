# 11000번 강의실 배정 (Greedy) 
# https://www.acmicpc.net/problem/11000

import heapq

N = int(input())
lectureInfo = []
for i in range(N):
    start, end = map(int, input().split())
    lectureInfo.append((start, end))

lectureInfo.sort()
timeTable = []
heapq.heappush(timeTable, lectureInfo[0][1])

for i in range(1, N):
    if lectureInfo[i][0] < timeTable[0]:
        heapq.heappush(timeTable, lectureInfo[i][1])
    else:
        heapq.heappop(timeTable)
        heapq.heappush(timeTable, lectureInfo[i][1])
        
print(len(timeTable))