# 백준 11726 2×n 타일링

import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * n

for i in range(1, n):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n - 1] % 10007)