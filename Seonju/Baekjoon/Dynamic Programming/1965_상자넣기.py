# 백준 1965 상자넣기

import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if box[j] < box[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))