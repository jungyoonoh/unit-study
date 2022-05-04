# 16497번 대출 요청 (Implementation) 
# https://www.acmicpc.net/problem/16497

import itertools

N = int(input())
info = [0] * 33 # 최대 31일까지

for _ in range(N):
    start, end = map(int, input().split())
    info[start] += 1
    info[end] -= 1

accSum = itertools.accumulate(info)
K = int(input())

print(0 if max(accSum) > K else 1)