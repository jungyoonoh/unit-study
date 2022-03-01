# 백준 15652 N과 M (4)

import sys
input = sys.stdin.readline


def dfs(cnt, former):  # 직전에 former를 선택했고, 현재까지 cnt개 선택한 상태에서 arr[cnt] 고르는 함수
    if cnt == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n + 1):
        if i >= former:
            arr[cnt] = i
            dfs(cnt + 1, i)


n, m = map(int, input().split())
arr = [0 for _ in range(m)]
dfs(0, 0)