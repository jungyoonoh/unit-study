# 백준 17836 공주님을 구해라!

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, dst_x, dst_y, time):
    q = deque([(x, y, time)])
    visited = [[0] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y, time = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and (graph[nx][ny] == 0 or graph[nx][ny] == 2) and not visited[nx][ny]:
                if nx == dst_x and ny == dst_y:
                    return time+1
                visited[nx][ny] = 1
                q.append((nx, ny, time+1))
    return float('inf')


n, m, t = map(int, input().split())
graph = [[] for _ in range(n)]
knife = ()
for i in range(n):
    graph[i] = list(map(int, input().split()))
    if 2 in graph[i]:
        knife = (i, graph[i].index(2))

# 칼 사용 X
not_use_knife = bfs(0, 0, n-1, m-1, 0)

# 칼 사용
tmp = bfs(0, 0, knife[0], knife[1], 0)
if tmp != float('inf'):
    use_knife = tmp + abs(n-1 - knife[0]) + abs(m-1 - knife[1])
else:
    use_knife = tmp

ans = min(not_use_knife, use_knife)

if ans <= t:
    print(ans)
else:
    print('Fail')
