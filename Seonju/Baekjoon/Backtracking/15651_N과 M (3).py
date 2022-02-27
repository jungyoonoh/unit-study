# 백준 15651 N과 M (3)

import sys
input = sys.stdin.readline


def back(cnt):
    if cnt == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n + 1):
        arr[cnt] = i
        back(cnt + 1)


n, m = map(int, input().split())
arr = [0 for _ in range(m)]
back(0)  # 0개 택한 상태에서 arr[0] 고르는 함수
