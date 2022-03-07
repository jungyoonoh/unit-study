# 백준 15655 N과 M (6)

import sys
input = sys.stdin.readline


def dfs(cnt, former): # cnt개 뽑은 상황에서 arr[cnt] 고르는 함수
    if cnt == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(former + 1, n):
        arr[cnt] = nums[i]
        dfs(cnt+1, i)


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = [0] * m

dfs(0, -1)