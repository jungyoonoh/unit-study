# 백준 15665 N과 M (11)

import sys
input = sys.stdin.readline


def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    former = 0
    for i in range(n):
        if nums[i] != former:
            arr.append(nums[i])
            former = nums[i]
            dfs()
            arr.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = []

dfs()
