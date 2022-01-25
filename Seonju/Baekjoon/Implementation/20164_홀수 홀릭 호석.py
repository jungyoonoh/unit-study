# 백준 20164 홀수 홀릭 호석

import sys
input = sys.stdin.readline

cnt = 0
minimum, maximum = float('inf'), float('-inf')


def split_two(n):
    global cnt
    if n < 10:
        if n % 2:
            cnt += 1
    else:
        if (n // 10) % 2: # 십의자리 숫자가 홀수면
            cnt += 1
        if (n % 10) % 2: # 일의자리 숫자가 홀수면
            cnt += 1
        split_two(n // 10 + n % 10)


def split_three(n, cnt_origin):
    global cnt, minimum, maximum

    if n < 10:
        if n % 2:
            cnt += 1

    elif n < 100:
        if (n // 10) % 2: # 십의자리 숫자가 홀수면
            cnt += 1
        if (n % 10) % 2: # 일의자리 숫자가 홀수면
            cnt += 1
        split_three(n // 10 + n % 10, cnt)

    else:
        n = str(n)
        for i in n:
            if int(i) % 2:
                cnt_origin += 1
        for i in range(1, len(n)-1):
            for j in range(i+1, len(n)):
                cnt = cnt_origin
                split_three(int(n[:i]) + int(n[i:j]) + int(n[j:]), cnt)
                minimum = min(minimum, cnt)
                maximum = max(maximum, cnt)


n = int(input())
if n < 10:
    print('1 1' if n%2 else '0 0')
elif n < 100:
    split_two(n)
    print(cnt, cnt)
else:
    split_three(n, 0)
    print(minimum, maximum)