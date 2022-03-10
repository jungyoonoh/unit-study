# 백준 15666 N과 M (12)

import sys
input = sys.stdin.readline


def dfs(idx):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    former = 0
    for i in range(idx, n):
        if nums[i] != former:
            arr.append(nums[i])
            former = nums[i]
            dfs(i)
            arr.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = []

dfs(0)
