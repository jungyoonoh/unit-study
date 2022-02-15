# 백준 11055 가장 큰 증가 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# 1, 100, 2, 50, 60, 3, 5, 6, 7, 8

dp = array.copy()
for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + array[i])

print(max(dp))