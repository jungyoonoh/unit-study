# 백준 15649 N과 M (1)

import sys
input = sys.stdin.readline


def back_tracking(cnt):
    if cnt == m:
        # 종료
        for j in range(m):
            print(arr[j], end=' ')
        print()
        return

    for i in range(1, n + 1):
        if not isUsed[i]:
            arr[cnt] = i
            isUsed[i] = 1
            back_tracking(cnt + 1)
            isUsed[i] = 0


n, m = map(int, input().split())
arr = [0 for _ in range(10)]  # 출력할 배열
isUsed = [0 for _ in range(10)]  # 숫자 i를 썼는지 체크하는 불린배열

back_tracking(0)  # 0개 택한 상황에서 arr[0]을 정하는 함수

