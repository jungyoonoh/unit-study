# 백준 15650 N과 M (2)

import sys
input = sys.stdin.readline


def dfs(idx):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(idx+1, n+1):
        arr.append(i)
        dfs(i)
        arr.pop()


n, m = map(int, input().split())
arr = []
dfs(0)