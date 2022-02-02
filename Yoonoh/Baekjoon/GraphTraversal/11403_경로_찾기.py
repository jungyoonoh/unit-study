# 11403번 경로 찾기 (Graph) 
# https://www.acmicpc.net/problem/11403

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for mid in range(N):
    for start in range(N):
        for end in range(N):
            if board[start][mid] == 1 and board[mid][end] == 1:
                board[start][end] = 1

for i in range(N):
    print(*board[i])