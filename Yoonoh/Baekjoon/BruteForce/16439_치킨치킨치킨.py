# 16439번 치킨치킨치킨 (BruteForce) 
# https://www.acmicpc.net/problem/16439

import itertools

N, M = map(int, input().split())
like = [list(map(int, input().split())) for _ in range(N)]

chickenNum = [i for i in range(M)]
case = list(itertools.combinations(chickenNum, 3))

res = 0
for c1, c2, c3 in case:
    s = 0   
    for i in range(N):
        s += max(like[i][c1], like[i][c2], like[i][c3])
        
    res = max(res, s)

print(res)