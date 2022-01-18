# 백준 16953 A → B

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 1

while a != b:
    if b % 2 != 0: # 홀수면
        if str(b)[len(str(b))-1] == '1' and b != 1: # 끝자리가 1이면 1 제거
            b = int(str(b)[:len(str(b))-1])
            cnt += 1
        else: # 아니면 -1 출력
            cnt = -1
            break
    elif b % 2 == 0: # 짝수면 나누기 2
        b //= 2
        cnt += 1

print(cnt)