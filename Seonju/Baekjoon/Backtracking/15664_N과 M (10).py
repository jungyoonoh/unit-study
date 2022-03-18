# 백준 15664 N과 M (10)

import sys
input = sys.stdin.readline


def dfs(idx):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    former = 0
    for i in range(idx+1, n):
        if not isUsed[i] and nums[i] != former:
            arr.append(nums[i])
            isUsed[i] = 1
            former = nums[i]
            dfs(i)
            arr.pop()
            isUsed[i] = 0


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = []
isUsed = [0] * n

dfs(-1)
