from collections import deque

visit = [0]*(100001)
queue = deque()

def BFS(start, goal):
    queue.append(start)

    while queue:
        x = queue.popleft()
        if x == goal:
            print(visit[x])
            break
        for nx in (x-1, x+1, 2*x):
            if (0<=nx<=100000) and not visit[nx]:
                visit[nx] = visit[x] + 1
                queue.append(nx)

n, k = map(int, input().split())
BFS(n, k)