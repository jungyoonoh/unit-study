# 2206번 벽 부수고 이동하기 (Graph) 
# https://www.acmicpc.net/problem/2206

from collections import deque

N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)] # 0 : 이동가능, 1 : 벽
isVisited = [[[0, 0] for _ in range(M)] for _ in range(N)] # 이 위치를 벽을 깨면서 갔는지 혹은 아닌지.
flag = False
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def move():
    dq = deque()
    dq.append((0, 0, 0)) # y, x, canBreak
    isVisited[0][0][0] = 1
    while dq:
        y, x, isBreak = dq.popleft()

        if y == N - 1 and x == M - 1:
            return isVisited[y][x][isBreak]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            
            if board[ny][nx] == 0 and isVisited[ny][nx][isBreak] == 0:
                dq.append((ny, nx, isBreak))
                isVisited[ny][nx][isBreak] = isVisited[y][x][isBreak] + 1
            
            if board[ny][nx] == 1 and isBreak == 0:
                dq.append((ny, nx, isBreak + 1))
                isVisited[ny][nx][isBreak + 1] = isVisited[y][x][isBreak] + 1    
                            
    return -1

print(move())