# 백준 15654 N과 M (5)

import sys
input = sys.stdin.readline


def dfs(cnt): # cnt개 선택한 상황에서 arr[cnt] 구하는 함수
    if cnt == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(n):
        if not isUsed[i]:
            arr[cnt] = nums[i]
            isUsed[i] = 1
            dfs(cnt + 1)
            isUsed[i] = 0


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = [0] * m
isUsed = [0] * n

dfs(0)