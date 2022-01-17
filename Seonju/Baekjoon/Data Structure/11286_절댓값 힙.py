# 백준 11286 절댓값 힙

import sys, heapq
input = sys.stdin.readline

h = []

for i in range(int(input())):
    x = int(input())
    if x != 0:
        heapq.heappush(h, (abs(x), x))
    else:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h)[1])