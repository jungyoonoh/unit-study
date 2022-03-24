# 백준 10211 Maximum Subarray

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    dp = [0] * n  # dp[i]는 i번째 수를 포함하는 부분수열의 합의 최댓값
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1]+nums[i])
    print(max(dp))
