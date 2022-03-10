# 7569번 토마토 (BFS) 
# https://www.acmicpc.net/problem/7569

from collections import deque

M, N, H = map(int, input().split()) # 가로 세로 높이
board = [[[] for _ in range(N)] for _ in range(H)]
dq = deque()

dx = [-1, 1, 0, 0, 0, 0] 
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
allTomatoRipen = True

for i in range(H):
    for j in range(N):
        data = list(map(int, input().split()))
        result = list(filter(lambda x: data[x] == 1, range(len(data)))) # 위치 1인 녀석만 찾기
        board[i][j].extend(data)

        for k in result:
            dq.append((i, j, k, 0))

        if allTomatoRipen and 0 in data:
            allTomatoRipen = False

if allTomatoRipen:
    print(0)
    exit(0)    

def checkTomato():
    maxVal = -1
    while dq:
        z, y, x, day = dq.popleft()
        maxVal = max(maxVal, day)
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if nx < 0 or ny < 0 or nz < 0 or nx >= M or ny >= N or nz >= H:
                continue
            
            if board[nz][ny][nx] != 0:
                continue
            
            board[nz][ny][nx] = 1
            dq.append((nz, ny, nx, day + 1))
        
    return maxVal

maxDay = checkTomato()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 0:
                print(-1)
                exit(0)

print(maxDay)