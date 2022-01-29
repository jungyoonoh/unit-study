# 24392번 영재의 징검다리 (DP) 
# https://www.acmicpc.net/problem/24392

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]

v = [-1, 0, 1]

for i in range(M):
    if board[-1][i] == 1:
        dp[-1][i] += 1

for i in range(N-2, -1, -1):
    for j in range(M):
        if board[i][j] == 1:
            for dir in v:
                if j + dir >= 0 and j + dir < M:
                    dp[i][j] += dp[i+1][j+dir] % 1_000_000_007

print(sum(dp[0]) % 1_000_000_007)