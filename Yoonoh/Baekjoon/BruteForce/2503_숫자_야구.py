# 2503번 숫자 야구 (BruteForce)
# https://www.acmicpc.net/problem/2503

import itertools

N = int(input())

numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
candidate = list(itertools.permutations(numList, 3))

for _ in range(N):
    info, strike, ball = map(int, input().split())
    info = list(str(info))
    
    removeNum = 0
    for i in range(len(candidate)):
        s = b = 0
        i -= removeNum
        for j in range(3):
            if info[j] == candidate[i][j]:
                s += 1
                continue
            if info[j] in candidate[i]:
                b += 1
        
        if strike != s or ball != b:
            candidate.remove(candidate[i])
            removeNum += 1

print(len(candidate))