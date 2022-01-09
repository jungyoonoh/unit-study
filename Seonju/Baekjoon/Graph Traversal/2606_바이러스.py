# 백준 2606 바이러스

import sys
input = sys.stdin.readline


def dfs(graph, visited, start):
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i)


if __name__ == '__main__':
    n = int(input())
    pair = int(input())

    graph = [[] for _ in range(n + 1)]

    for i in range(pair):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n + 1)
    dfs(graph, visited, 1)

    print(visited.count(1) - 1)
