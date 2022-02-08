# 백준 11279 최대 힙

import sys, heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    a = int(input())
    if a:
        heapq.heappush(q, -a)
    elif not q:
        print(0)
    else:
        print(-heapq.heappop(q))