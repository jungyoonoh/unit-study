# 백준 14719 빗물

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
water = list(map(int, input().split()))
blocks = [[0] * w for _ in range(h)]

for i in range(w):
    for j in range(water[0]):
        blocks[j][i] = 1
    del water[0]

ans = 0
for block in blocks:
    if not (sum(block) == 0 or sum(block) == w):
        start = block.index(1)
        subSum = 0
        for i in range(start, w):
            if block[i] == 0:
                subSum += 1
            if block[i] == 1:
                ans += subSum
                subSum = 0

print(ans)