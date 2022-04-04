# 백준 18232 텔레포트 정거장

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque([(0, s)])
    visited[s] = 1
    while q:
        time, x = q.popleft()
        for nx in [x-1, x+1, *warp[x]]:
            if 1 <= nx <= n and not visited[nx]:
                if nx == e:
                    print(time+1)
                    return
                q.append((time+1, nx))
                visited[nx] = 1


n, m = map(int, input().split())  # n은 위치 갯수, m은 텔레포트 연결정보 갯수
s, e = map(int, input().split())  # s는 출발지, e는 도착지

warp = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    warp[a].append(b)
    warp[b].append(a)

bfs()
