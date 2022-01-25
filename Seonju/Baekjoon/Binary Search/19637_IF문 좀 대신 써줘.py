# 백준 19637 IF문 좀 대신 써줘

import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())
title = []
power = []

for _ in range(n):
    a, b = input().split()
    title.append(a)
    power.append(int(b))

for _ in range(m):
    print(title[bisect_left(power, int(input()))])
