# 2573번 빙산 (BruteForce) 
# https://www.acmicpc.net/problem/2573

from collections import deque

N, M = map(int, input().split()) # 세로, 가로
board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0] # 12 3 6 9
dx = [0, 1, 0, -1]

def melt():
    temp = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if board[i][j]: # 빙산이면
                cnt = 0
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                
                    if board[ny][nx] == 0:
                        cnt += 1
                        
                val = board[i][j] - cnt if board[i][j] - cnt > 0 else 0
                temp[i][j] = val                
            else:
                temp[i][j] = board[i][j]
                          
    return temp

def searchIce(i, j, isVisited):
    dq = deque()
    
    dq.append((i, j))
    isVisited[i][j] = True
    while dq:
        y, x = dq.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            
            if isVisited[ny][nx] or board[ny][nx] == 0:
                continue
            
            isVisited[ny][nx] = True
            dq.append((ny, nx))    
            
year = 0
flag = False
while True:    
    beforeSearch = False
    isVisited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not isVisited[i][j]:
                if not beforeSearch:
                    beforeSearch = True
                    searchIce(i, j, isVisited)
                else:
                    print(year)
                    exit(0)
    
    board = melt()
    year += 1

    if not beforeSearch: # 한번도 찾지 못할경우 == 다녹음
        print(0)
        break