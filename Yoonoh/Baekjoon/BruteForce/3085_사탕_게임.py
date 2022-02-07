# 3085번 사탕 게임 (BruteForce) 
# https://www.acmicpc.net/problem/3085

N = int(input())
board = [list(input()) for _ in range(N)]

dy = [-1, 0, 1, 0] # 12 3 6 9
dx = [0, 1, 0, -1]

def cntCandy():
    M = -1
    for i in range(N):
        cnt = 0
        for j in range(N - 1):
            if board[i][j] == board[i][j + 1]:
                cnt += 1
            else:
                M = max(cnt, M)
                cnt = 0
        M = max(cnt, M)
            
    for i in range(N):
        cnt = 0
        for j in range(N - 1):
            if board[j][i] == board[j + 1][i]:
                cnt += 1
            else:
                M = max(cnt, M)
                cnt = 0        
        M = max(cnt, M)    
    
    return M + 1
    
def selectCandy(y, x):
    M = -1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue
        
        board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
        M = max(M, cntCandy())
        board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
        
        
    return M

maxVal = -1
for i in range(N):
    for j in range(N):
        maxVal = max(maxVal, selectCandy(i, j))

print(maxVal)