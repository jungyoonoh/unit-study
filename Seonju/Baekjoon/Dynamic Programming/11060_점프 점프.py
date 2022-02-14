# 백준 11060 점프 점프

import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input())
pos = list(map(int, input().split()))

dp = [INF] * n  # i번째 칸까지 올 수 있으면 점프 최소횟수로 갱신
dp[0] = 0

for i in range(1, n):
    for j in range(0, i):
        if j + pos[j] >= i:
            dp[i] = min(dp[i], dp[j] + 1)

print(dp[n - 1] if dp[n - 1] != INF else -1)
