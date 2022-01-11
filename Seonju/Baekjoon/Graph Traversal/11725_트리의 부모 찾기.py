# 백준 11725 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            parent[i] = node
            dfs(i)


if __name__ == '__main__':
    n = int(input())

    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    parent = [0] * (n+1)

    while True:
        try:
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        except:
            break

    for i in range(n+1):
        graph[i].sort()

    dfs(1)

    print(*parent[2:], sep='\n')
