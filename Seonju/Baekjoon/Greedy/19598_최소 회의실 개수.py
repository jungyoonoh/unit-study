# 백준 19598 최소 회의실 개수

import sys, heapq
input = sys.stdin.readline

meeting = []
for _ in range(int(input())):
    meeting.append(list(map(int, input().split())))
meeting.sort()

room = []
heapq.heappush(room, meeting[0][1])

for start, end in meeting[1:]:
    if room[0] <= start:
        heapq.heapreplace(room, end)
    else:
        heapq.heappush(room, end)

print(len(room))