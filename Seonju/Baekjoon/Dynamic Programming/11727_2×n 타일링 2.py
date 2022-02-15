# 백준 11727 2×n 타일링 2

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * n
if n == 1:
    print(1)
else:
    dp[0] = 1
    dp[1] = 3

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2] * 2

    print(dp[n - 1] % 10007)