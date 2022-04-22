from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
graph[0] = [0, 0]
visited = [False for _ in range(n+1)]

def DFS(start):
    visited[start] = True
    print(start, end = " ")

    for i in graph[start]:
        if not visited[i]:
            DFS(i)

def BFS(start):
    visited[start] = True
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        print(vertex, end = " ")
        for i in graph[vertex]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

DFS(v)
print()
visited = [False for _ in range(n+1)]
BFS(v)