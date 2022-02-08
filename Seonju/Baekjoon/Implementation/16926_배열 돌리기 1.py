# 백준 16926 배열 돌리기 1

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    graph_new = [[0 for _ in range(m)] for _ in range(n)]

    for start in range(0, min(n, m) // 2):
        end_r = n - 1 - start
        end_c = m - 1 - start

        # left
        for a in range(start+1, end_c+1):
            graph_new[start][a-1] = graph[start][a]
        # down
        for a in range(start, end_r):
            graph_new[a+1][start] = graph[a][start]
        # right
        for a in range(start, end_c):
            graph_new[end_r][a+1] = graph[end_r][a]
        # up
        for a in range(start+1, end_r+1):
            graph_new[a-1][end_c] = graph[a][end_c]

    graph = graph_new.copy()

for i in graph:
    print(*i, sep=' ')