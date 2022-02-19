# 2210번 숫자판 점프 (BruteForce) 
# https://www.acmicpc.net/problem/2210

from collections import deque

board = [list(map(int, input().split())) for _ in range(5)]
pool = set()
dy = [-1, 0, 1, 0] # 12 3 6 9
dx = [0, 1, 0, -1]
def search(y, x):
    dq = deque()
    dq.append((y,x,str(board[y][x])))
    
    while dq:
        y, x, ns = dq.popleft()
        
        if len(ns) == 6:
            pool.add(ns)
            continue
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= 5 or nx >= 5:
                continue
            
            dq.append((ny, nx, ns + str(board[ny][nx])))

for i in range(5):
    for j in range(5):
        search(i, j)

print(len(list(pool)))