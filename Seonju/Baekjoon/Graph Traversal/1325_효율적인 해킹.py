# 백준 1325 효율적인 해킹

import sys
from collections import deque
input = sys.stdin.readline


def bfs(node):
    q = deque([node])
    visited = [0] * (n + 1)
    visited[node] = 1
    cnt = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)

    maximum = 0
    idx = []

    for i in range(1, n + 1):
        ret = bfs(i)
        if maximum < ret:
            idx = [i]
            maximum = ret
        elif maximum == ret:
            idx.append(i)

    print(*idx, sep=' ')
