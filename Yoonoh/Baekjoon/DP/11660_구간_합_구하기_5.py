# 11660번 구간 합 구하기 5 (DP) 
# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 한 변, 합을 구해야 하는 횟수 
board = [list(map(int, input().split())) for _ in range(N)]
total = [[0 for _ in range(N)] for _ in range(N)]
total[0][0] = board[0][0]

for i in range(1, N):
    total[i][0] = board[i][0] + total[i-1][0]
    total[0][i] = board[0][i] + total[0][i-1]
 
for i in range(1, N):
    for j in range(1, N):
        total[i][j] = board[i][j] + total[i-1][j] + total[i][j-1] - total[i-1][j-1]

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    y1, x1, y2, x2 = y1-1, x1-1, y2-1, x2-1

    if x1 == 0 and y1 == 0:
        print(total[y2][x2])
        continue
    
    if x1 == 0:
        print(total[y2][x2] - total[y1-1][x2])
        continue
    
    if y1 == 0:
        print(total[y2][x2] - total[y2][x1-1])
        continue
    
    print(total[y2][x2] - total[y2][x1-1] - total[y1-1][x2] + total[y1-1][x1-1])