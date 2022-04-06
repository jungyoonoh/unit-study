# 20437번 문자열 게임 2 (String) 
# https://www.acmicpc.net/problem/20437

import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

def stringGame(alphaCnt, alphaIdx, K):
    maxVal = -1
    minVal = 10001
    for i in alphaCnt.keys():
        if alphaCnt[i] >= K:
            for j in range(len(alphaIdx[i]) - K + 1):
                maxVal = max(maxVal, alphaIdx[i][j + K - 1] - alphaIdx[i][j] + 1)
                minVal = min(minVal, alphaIdx[i][j + K - 1] - alphaIdx[i][j] + 1)
            
    return maxVal, minVal

for _ in range(T):
    alphaCnt = defaultdict(int)
    alphaIdx = defaultdict(list)
    S = input().strip()
    K = int(input())
    
    for i in range(len(S)):
        alphaCnt[S[i]] += 1
        alphaIdx[S[i]].append(i)
    
    maxVal, minVal = stringGame(alphaCnt, alphaIdx, K)
    if maxVal == -1 and minVal == 10001:
        print(-1)
    else:
        print(minVal, maxVal)