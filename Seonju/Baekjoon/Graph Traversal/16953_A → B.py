# 백준 16953 A → B
# Greedy로 풀었던 문젠데 BFS로 다시 풀어보았읍니다

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque([(a, 1)])
    while q:
        x, dist = q.popleft()
        if x == b:
            print(dist)
            sys.exit(0)
        for nx in [x * 2, int(str(x) + '1')]:
            if nx <= b:
                q.append((nx, dist + 1))
    print(-1)


a, b = map(int, input().split())
bfs()
