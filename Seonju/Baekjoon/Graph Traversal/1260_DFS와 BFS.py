# 백준 1260 DFS와 BFS

import sys
from collections import deque
input = sys.stdin.readline


def dfs(node):
    print(node, end=' ')
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


def bfs(node):
    q = deque([node])
    visited[node] = 1
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1


if __name__ == '__main__':
    n, edge, start = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for _ in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(n + 1):
        graph[i].sort()

    dfs(start)
    print()
    visited = [0] * (n + 1)
    bfs(start)
