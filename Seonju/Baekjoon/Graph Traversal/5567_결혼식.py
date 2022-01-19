# 백준 5567 결혼식

import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    cnt = 0
    visited[start] = 1
    q = deque([(start, 0)])

    while q:
        now, dist = q.popleft()
        if dist <= 2:
            cnt += 1
        for v in graph[now]:
            if not visited[v]:
                visited[v] = 1
                q.append((v, dist + 1))

    return cnt - 1


if __name__ == '__main__':
    n = int(input()) # 동기 수
    m = int(input()) # 친구 관계 수

    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(1))