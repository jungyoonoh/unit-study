# 백준 15724 주지수

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(m):
        dp[i][j] += dp[i-1][j]

for _ in range(int(input())):
    fromX, fromY, toX, toY = map(int, input().split())
    ans = sum(dp[toX-1][fromY-1:toY])
    if fromX > 1:
        ans -= sum(dp[fromX-2][fromY-1:toY])
    print(ans)
