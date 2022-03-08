# 백준 13908 비밀번호

import sys
input = sys.stdin.readline


def dfs():
    global ans
    if len(arr) == n:
        if not set(code)-set(arr):
            ans += 1
        return
    for i in range(10):
        arr.append(i)
        dfs()
        arr.pop()


n, m = map(int, input().split())
code = list(map(int, input().split()))
arr = []

ans = 0
dfs()
print(ans)
