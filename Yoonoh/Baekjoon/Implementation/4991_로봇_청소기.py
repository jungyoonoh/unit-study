# 4991번 로봇 청소기 (Implementation) 
# https://www.acmicpc.net/problem/4991

import itertools
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def findDust(board, W, H):
    dust = []
    for i in range(H):
        for j in range(W):
            if board[i][j] == '*':
                dust.append([i, j])
            elif board[i][j] == 'o':
                dust.insert(0, [i, j])

    return dust

def setDistanceBetweenDust(board, dust, L, W, H):
    
    distanceBetweenDust = [[0 for _ in range(L)] for _ in range(L)]
    
    for i in range(L):
        dq = deque()
        dq.append((dust[i][0], dust[i][1]))
        
        isVisited = [[False for _ in range(W)] for _ in range(H)]
        dist = [[-1 for _ in range(W)] for _ in range(H)]
        
        isVisited[dust[i][0]][dust[i][1]] = True
        dist[dust[i][0]][dust[i][1]] = 0
        
        while dq:
            y, x = dq.popleft()

            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                
                if ny < 0 or nx < 0 or ny >= H or nx >= W:
                    continue
                
                if isVisited[ny][nx] or board[ny][nx] == 'x':
                    continue
                
                isVisited[ny][nx] = True
                dist[ny][nx] = dist[y][x] + 1
                dq.append((ny, nx))
        
        for j in range(L):
            distanceBetweenDust[i][j] = dist[dust[j][0]][dust[j][1]]
    
    flag = True
    for i in range(L):
        if distanceBetweenDust[i].count(-1) >= 1:
            flag = False
            
    return distanceBetweenDust, flag

def findShortestPath(dist, L):
    minVal = 400 * 10 
    candidate = list(itertools.permutations([i for i in range(1, L)], L - 1))    
    
    for seq in candidate:
        start, d = 0, 0
        
        for i in seq:
            d += dist[start][i]
            start = i
        
        minVal = min(minVal, d)
            
    return minVal

while True:
    W, H = map(int, input().split()) # 가로 세로    
    board = [list(input()) for _ in range(H)]
    if W == 0 and H == 0:
        break
    
    dust = findDust(board, W, H)
    L = len(dust)

    dist, flag = setDistanceBetweenDust(board, dust, L, W, H)
    print(findShortestPath(dist, L) if flag else -1)