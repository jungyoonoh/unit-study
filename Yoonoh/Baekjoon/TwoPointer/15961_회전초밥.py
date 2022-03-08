# 15961번 회전초밥 (TwoPointer) 
# https://www.acmicpc.net/problem/15961

import sys
from collections import defaultdict
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
dd = defaultdict(int)
dd[c] += 1
for i in range(k):
    dd[sushi[i]] += 1
    sushi.append(sushi[i])
maxVal = len(dd.keys())

for i in range(k, N+k):
    dd[sushi[i]] += 1
    if dd[sushi[i-k]] == 1:
        dd.pop(sushi[i - k])
    else:
        dd[sushi[i-k]] -= 1
    maxVal = max(maxVal, len(dd.keys()))

print(maxVal)