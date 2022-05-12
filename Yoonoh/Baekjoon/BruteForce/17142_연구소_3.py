# 17142번 연구소 3 (BruteForce) 
# https://www.acmicpc.net/problem/17142

import itertools
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
candidateOfVirusPosition = []

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            candidateOfVirusPosition.append((i, j))

def spreadVirus(virus, isVisited, timeTable):
    
    dq = deque()

    for y, x in virus:
        dq.append((y, x, 0))
        isVisited[y][x] = True
    
    while dq:
        y, x, time = dq.popleft()
        
        timeTable[y][x] = time
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            
            if board[ny][nx] == 1 or isVisited[ny][nx]:
                continue        
            
            isVisited[ny][nx] = True
            dq.append((ny, nx, time + 1))
    
    for i in range(N):
        for j in range(N):
            if not isVisited[i][j]:
                return 2501
    
    maxTimeVal = -1
    for i in range(N):
        for j in range(N):
            if timeTable[i][j] != -1 and board[i][j] == 0:
                maxTimeVal = max(maxTimeVal, timeTable[i][j])
        
    return maxTimeVal

pos = list(itertools.combinations(candidateOfVirusPosition, M))

minimumValue = 2501
for candidate in pos:
    minimumValue = min(minimumValue, spreadVirus(
        candidate, 
        [[False if board[i][j] != 1 else True for j in range(N)] for i in range(N)],
        [[-1 for _ in range(N)] for _ in range(N)]))

flag = False
for i in range(N):
    if 0 in board[i]:
        flag = True
        break

if flag:
    print(minimumValue if minimumValue != 2501 else -1)
else: print(0)