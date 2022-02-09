# 백준 11722 가장 긴 감소하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

d = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if a[i] < a[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))