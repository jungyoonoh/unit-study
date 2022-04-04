# 15724번 주지수 (DP) 
# https://www.acmicpc.net/problem/15724

N, M = map(int, input().split()) # 세로 가로 
board = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
total = [[0 for _ in range(M)] for _ in range(N)]
total[0][0] = board[0][0]

for i in range(1, N):
    total[i][0] = board[i][0] + total[i-1][0]

for i in range(1, M):
    total[0][i] = board[0][i] + total[0][i-1]
 
for i in range(1, N):
    for j in range(1, M):
        total[i][j] = board[i][j] + total[i-1][j] + total[i][j-1] - total[i-1][j-1]

for _ in range(K):
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