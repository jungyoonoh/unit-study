# 2583번 영역 구하기 (BruteForce) 
# https://www.acmicpc.net/problem/2583

from collections import deque

N, M, K = map(int, input().split()) # 세로 가로 K개의 직사각형
board = [[0 for _ in range(M)] for _ in range(N)]
isVisited = [[False for _ in range(M)] for _ in range(N)]

dy = [-1, 0, 1, 0] # 12 3 6 9
dx = [0, 1, 0, -1]

def searchSquare(i, j):
    dq = deque()
    dq.append((i, j))
    cnt = 1
    isVisited[i][j] = True
    while dq:
        y, x = dq.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            
            if isVisited[ny][nx] or board[ny][nx] == 1:
                continue
            
            isVisited[ny][nx] = True
            dq.append((ny, nx))
            cnt += 1
            
    return cnt

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            board[k][j] = 1

sector = 0
area = []
for i in range(N):
    for j in range(M):
        if not isVisited[i][j] and board[i][j] == 0:
            area.append(searchSquare(i, j))
            sector += 1

area.sort()
print(sector)
print(*area)