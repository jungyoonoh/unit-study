# 1937번 욕심쟁이 판다 (DP) 
# https://www.acmicpc.net/problem/1937

from collections import deque
import sys
sys.setrecursionlimit(10**6)
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def move(y, x):
    if dp[y][x]:
        return dp[y][x]
    
    dp[y][x] = 1
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue
        
        if board[ny][nx] > board[y][x]:
            dp[y][x] = max(dp[y][x], move(ny, nx) + 1) # 현재 위치에서 갈 수 있는지.

    return dp[y][x]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(move(i, j), ans)
    
print(ans)