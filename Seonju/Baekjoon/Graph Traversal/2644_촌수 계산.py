# 백준 2644 촌수 계산

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque([a])
    while q:
        v = q.popleft()
        for now in graph[v]:
            if now == b:
                print(dist[v] + 1)
                sys.exit(0)
            if not dist[now]:
                dist[now] = dist[v] + 1
                q.append(now)
    print(-1)


# 사람 수
n = int(input())
graph = [[] for _ in range(n+1)]
dist = [0 for _ in range(n+1)]

a, b = map(int, input().split())

# 관계 수
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs()