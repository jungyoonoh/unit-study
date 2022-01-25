# 20164번 홀수 홀릭 호석 (Implementation) 
# https://www.acmicpc.net/problem/20164

import itertools

N = list(input())

minVal, maxVal = 10e9, -1

def cntOdd(val):
    cnt = 0
    for i in range(len(val)):
        if int(val[i]) % 2 == 1:
            cnt += 1
    return cnt

def cutNum(num, cnt):
    global minVal, maxVal
    L, cnt = len(num), cntOdd(num)
    if L == 1:
        minVal, maxVal = min(minVal, cnt), max(maxVal, cnt)
        return
    
    if L == 2:
        nextNum = list(str(int(num[0]) + int(num[1])))
        cutNum(nextNum, cnt)
        return
    
    bound = [i for i in range(1, L)] # 1 ~ L - 1
    candidate = list(itertools.combinations(bound, 2))
    
    for c1, c2 in candidate:
        s1, s2, s3 = int(''.join(num[:c1])), int(''.join(num[c1:c2])), int(''.join(num[c2:]))
        nextNum = list(str(s1 + s2 + s3))
        cutNum(nextNum, cnt)
        
    return

cutNum(N, 0)
print(minVal, maxVal)