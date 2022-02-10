# 11048번 이동하기 (DP) 
# https://www.acmicpc.net/problem/11048

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]

dp[0][0] = board[0][0]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + board[i][0]

for i in range(1, M):
    dp[0][i] = dp[0][i-1] + board[0][i]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = board[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[N-1][M-1])