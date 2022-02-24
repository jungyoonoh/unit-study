# 백준 22857 가장 긴 짝수 연속한 부분 수열 (small)

import sys
input = sys.stdin.readline


n, k = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 0, 0
cnt_odd, cnt_even = 0, 0
maximum = 0

for start in range(n):
    while cnt_odd <= k and end < n:
        if lst[end] % 2:
            cnt_odd += 1
        else:
            cnt_even += 1
        end += 1
    if maximum < cnt_even:
        maximum = cnt_even
    if lst[start] % 2:
        cnt_odd -= 1
    else:
        cnt_even -= 1

print(maximum)