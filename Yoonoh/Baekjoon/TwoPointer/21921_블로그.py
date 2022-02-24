# 21921번 블로그 (TwoPointer) 
# https://www.acmicpc.net/problem/21921

import itertools

N, X = map(int,input().split())
info = list(map(int, input().split()))
maxVal = max(info)
accSum = list(itertools.accumulate(info))
cnt = 0

if maxVal == 0:
    print("SAD")
else:
    maxVal = accSum[X-1]
    for i in range(N-X):
        maxVal = max(maxVal, accSum[i+X] - accSum[i])
    
    if maxVal == accSum[X-1]:
        cnt += 1
    for i in range(N-X):
        if maxVal == (accSum[i+X] - accSum[i]):
            cnt += 1
    
    print(maxVal)
    print(cnt)