# 16937번 두 스티커 (BruteForce) 
# https://www.acmicpc.net/problem/16937

import itertools

H, W = map(int, input().split())
N = int(input())

sticker = [] # R, C
for i in range(N):
    R, C = map(int, input().split())
    sticker.append((R,C))
comb = list(itertools.combinations([i for i in range(N)], 2))

M = 0
for c1, c2 in comb:
    if (sticker[c1][0] + sticker[c2][0]) <= W and max(sticker[c1][1], sticker[c2][1]) <= H:
        M = max(M, sticker[c1][0] * sticker[c1][1] + sticker[c2][0] * sticker[c2][1])
        continue
    if (sticker[c1][0] + sticker[c2][1]) <= W and max(sticker[c1][1], sticker[c2][0]) <= H:
        M = max(M, sticker[c1][0] * sticker[c1][1] + sticker[c2][0] * sticker[c2][1])
        continue
    if (sticker[c1][1] + sticker[c2][0]) <= W and max(sticker[c1][0], sticker[c2][1]) <= H:
        M = max(M, sticker[c1][0] * sticker[c1][1] + sticker[c2][0] * sticker[c2][1])
        continue
    if (sticker[c1][1] + sticker[c2][1]) <= W and max(sticker[c1][0], sticker[c2][0]) <= H:
        M = max(M, sticker[c1][0] * sticker[c1][1] + sticker[c2][0] * sticker[c2][1])
        continue
    if (sticker[c1][0] + sticker[c2][0]) <= H and max(sticker[c1][1], sticker[c2][1]) <= W:
        M = max(M, sticker[c1][0] * sticker[c1][1] + sticker[c2][0] * sticker[c2][1])
        continue
    if (sticker[c1][0] + sticker[c2][1]) <= H and max(sticker[c1][1], sticker[c2][0]) <= W:
        M = max(M, sticker[c1][0] * sticker[c1][1] + sticker[c2][0] * sticker[c2][1])
        continue
    if (sticker[c1][1] + sticker[c2][0]) <= H and max(sticker[c1][0], sticker[c2][1]) <= W:
        M = max(M, sticker[c1][0] * sticker[c1][1] + sticker[c2][0] * sticker[c2][1])
        continue
    if (sticker[c1][1] + sticker[c2][1]) <= H and max(sticker[c1][0], sticker[c2][0]) <= W:
        M = max(M, sticker[c1][0] * sticker[c1][1] + sticker[c2][0] * sticker[c2][1])
        continue

print(M)