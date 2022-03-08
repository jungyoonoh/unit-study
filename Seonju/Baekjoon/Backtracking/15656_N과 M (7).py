# 백준 15656 N과 M (7)

import sys
input = sys.stdin.readline


def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(n):
        arr.append(nums[i])
        dfs()
        arr.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = []

dfs()