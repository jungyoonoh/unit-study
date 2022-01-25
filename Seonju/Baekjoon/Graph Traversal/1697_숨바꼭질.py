# 백준 1697 숨바꼭질

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque([n])

    while q:
        x = q.popleft()

        if x == k:
            print(dist[x])
            break

        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= 10**5 and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)


n, k = map(int, input().split())
dist = [0 for i in range(10**5 + 1)]  # 아놔 이거 +1 안해줘서 계속 틀림... 정신체리
bfs()
