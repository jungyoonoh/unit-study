# 19942번 다이어트 (BruteForce) 
# https://www.acmicpc.net/problem/19942

import itertools

N = int(input())
mp, mf, ms, mv = map(int, input().split())
ingredient = [(0,0,0,0,0)]
for _ in range(N):
    p, f, s, v, c = map(int, input().split())
    ingredient.append((p, f, s, v, c))

cost = 500 * 15 + 1
ans = []
candidate = []

for i in range(1, N+1):
    candidate.extend(list(itertools.combinations([i for i in range(1, N+1)], i)))
candidate.sort()

for comb in candidate:
    tp, tf, ts, tv, tc = 0, 0, 0, 0, 0
    for j in comb:
        tp += ingredient[j][0]            
        tf += ingredient[j][1]            
        ts += ingredient[j][2]            
        tv += ingredient[j][3]            
        tc += ingredient[j][4]
            
    if tp >= mp and tf >= mf and ts >= ms and tv >= mv and cost > tc:
        cost = tc
        ans = comb

if cost == 500 * 15 + 1:
    print(-1)
else:
    print(cost)
    print(*ans)