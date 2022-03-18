# 17129번 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유 (BFS) 
# https://www.acmicpc.net/problem/17129

from collections import deque

n, m = map(int, input().split())
dq = deque()
flag = False
board = []
isVisited = [[False for _ in range(m)] for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input()))
    board.append(data)
    if not flag and 2 in data:
        dq.append((i, data.index(2), 0))
        flag = True

canFind = False        
while dq:
    y, x, dist = dq.popleft()
    if board[y][x] == 3 or board[y][x] == 4 or board[y][x] == 5:
        print("TAK")
        print(dist)
        canFind = True
        break
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        
        if board[ny][nx] == 1 or isVisited[ny][nx]:
            continue
        
        dq.append((ny, nx, dist + 1))
        isVisited[ny][nx] = True
        
if not canFind:
    print("NIE")