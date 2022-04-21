import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
graph[0] = [0, 0]
count = 0

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

def DFS(s):
    visited[s] = True

    for j in graph[s]:
        if not visited[j]:
            DFS(j)

for x in range(1, n+1):
    if visited[x] == False:
        count = count + 1
        DFS(x)

print(count)