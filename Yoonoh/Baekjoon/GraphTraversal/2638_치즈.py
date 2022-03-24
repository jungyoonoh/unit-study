# 2638번 치즈 (Graph) 
# https://www.acmicpc.net/problem/2638

from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def getCheeseBoard(board):
    cheeseBoard = [[1 for _ in range(M)] for _ in range(N)]
    isVisited = [[False for _ in range(M)] for _ in range(N)]

    y, x = 0, 0
    dq = deque()
    dq.append((y, x))
    isVisited[y][x] = True
    cnt = 0
    
    while dq:
        y, x = dq.popleft()
        cnt += 1
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            
            if isVisited[ny][nx] or board[ny][nx] == 1:
                continue
            
            isVisited[ny][nx] = True
            dq.append((ny, nx))
            cheeseBoard[ny][nx] = 0
            
    return cheeseBoard, cnt == M * N

def melt(cheeseBoard):    
    meltingSpot = []
    
    for i in range(N):
        for j in range(M):
            if cheeseBoard[i][j] == 1:
                cnt = 0
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    
                    if ny < 0 or nx < 0 or ny >= N or nx >= M:
                        continue
                    
                    if cheeseBoard[ny][nx] == 0:
                        cnt += 1
                
                if cnt > 1:
                    meltingSpot.append((i, j))
    
    for y, x in meltingSpot:
        board[y][x] = 0
    
    return

time = 0
while True:
    cheeseBoard, flag = getCheeseBoard(board)

    if flag:
        print(time)
        break
    
    melt(cheeseBoard)
    time += 1