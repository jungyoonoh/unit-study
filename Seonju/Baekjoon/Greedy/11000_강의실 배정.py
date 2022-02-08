# 백준 11000 강의실 배정

import sys, heapq
input = sys.stdin.readline

n = int(input())
lesson = [list(map(int, input().split())) for i in range(n)]
lesson.sort()

room = []
heapq.heappush(room, lesson[0][1])

for i in range(1, len(lesson)):
    if room[0] > lesson[i][0]:
        heapq.heappush(room, lesson[i][1])
    else:
        heapq.heapreplace(room, lesson[i][1])

print(len(room))