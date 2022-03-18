# 백준 15663 N과 M (9)

import sys
input = sys.stdin.readline


def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    former = 0
    for i in range(n):
        if not isUsed[i] and nums[i] != former:
            arr.append(nums[i])
            isUsed[i] = 1
            former = nums[i]
            dfs()
            isUsed[i] = 0
            arr.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
isUsed = [0] * n
arr = []

dfs()
