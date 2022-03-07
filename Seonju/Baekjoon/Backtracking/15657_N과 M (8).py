# 백준 15657 N과 M (8)

import sys
input = sys.stdin.readline


def dfs(former):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(former+1, n):
        arr.append(nums[i])
        dfs(i-1)
        arr.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = []

dfs(-1)
