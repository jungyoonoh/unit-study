import sys
sys.setrecursionlimit(10000)

k = int(sys.stdin.readline())

def DFS(start):
    visited[start] = True
    for j in graph[start]:
        if not visited[j]:
            DFS(j)


for i in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    graph[0] = 0
    for j in range(e):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)
        graph[start].sort()
        graph[end].sort()
    for m in range(1, v+1):
        if (len(graph[m]) > 1):
            for n in graph[m]:
                if (graph[n] in graph[m]):
                    print("NO")
                    exit(0)
    print("YES")



