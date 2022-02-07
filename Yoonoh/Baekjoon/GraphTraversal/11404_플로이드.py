# 11404번 플로이드 (Graph) 
# https://www.acmicpc.net/problem/11404

import sys
input = sys.stdin.readline

maxVal = 1e12
N = int(input())
M = int(input())
board = [[int(maxVal) for _ in range(N)] for _ in range(N)]

for i in range(M):
    start, end, cost = map(int, input().split())
    board[start - 1][end - 1] = min(cost, board[start - 1][end - 1])

for i in range(N):
    board[i][i] = 0

for mid in range(N):
    for start in range(N):
        for end in range(N):
            board[start][end] = min(board[start][end], board[start][mid] + board[mid][end])
                
for i in range(N):
    for j in range(N):
        if board[i][j] == maxVal:
            print(0, end = ' ')
        else:
            print(board[i][j], end = ' ')
    print()