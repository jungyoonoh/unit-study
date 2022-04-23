from collections import deque
queue = deque([])

dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

tc = int(input())

def knight(start_x, start_y, end_x, end_y):

    if start_x == end_x and start_y == end_y:
        return 0
    queue.append([start_y, start_x])
    while queue :
        y, x = queue.popleft()
        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]

            if (0<=ny<l) and (0<=nx<l):
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    if ny == end_y and nx == end_x:
                        return graph[end_y][end_x]
                    queue.append([ny, nx])

for _ in range(tc):
    l = int(input())
    graph = [[0]*l for _ in range(l)]

    starty, startx = map(int, input().split())
    endy, endx = map(int, input().split())
    print(knight(startx, starty, endx, endy))
    queue.clear()