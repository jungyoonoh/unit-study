# 2636번 치즈 (Graph) 
# https://www.acmicpc.net/problem/2636

from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def findMeltingSpot(): 
    isVisited = [[False for _ in range(M)] for _ in range(N)]
    meltingSpot = []
    
    y, x = 0, 0
    
    dq = deque()
    dq.append((y, x))
    
    isVisited[y][x] = True
    
    while dq:
        y, x = dq.popleft()
                
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            
            if isVisited[ny][nx]:
                continue
            
            if board[ny][nx] == 1:
                meltingSpot.append((ny, nx))
                continue
            
            isVisited[ny][nx] = True
            dq.append((ny, nx))
        
    return meltingSpot

def melt(meltingSpot):
    
    cheeseCntBeforeMelt = 0
    for i in range(N):
        cheeseCntBeforeMelt += board[i].count(1)
    
    for y, x in meltingSpot:
        board[y][x] = 0
    
    remainCheese = 0
    for i in range(N):
        remainCheese += board[i].count(1)

    return cheeseCntBeforeMelt, remainCheese

time, remainCheese, result = 0, 0, 0
while True:
    meltingSpot = findMeltingSpot()
        
    before, now = melt(meltingSpot)
    time += 1
    
    if now == 0:
        print(time)
        print(before)
        break