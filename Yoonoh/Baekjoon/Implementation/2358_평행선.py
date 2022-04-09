# 2358번 평행선 (Implementation) 
# https://www.acmicpc.net/problem/2358

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
parallelX = defaultdict(list)
parallelY = defaultdict(list)
for i in range(N):
    y, x = map(int, input().split())
    parallelX[x].append(y)
    parallelY[y].append(x)

ans = 0
for i in parallelX.keys():
    if len(parallelX[i]) > 1:
        ans += 1

for i in parallelY.keys():
    if len(parallelY[i]) > 1:
        ans += 1

print(ans)