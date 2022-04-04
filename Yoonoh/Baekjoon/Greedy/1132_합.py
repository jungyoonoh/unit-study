# 1132번 합 (Greedy) 
# https://www.acmicpc.net/problem/1132

import sys
input = sys.stdin.readline
N = int(input().strip())
M = 10
canBeZero = [True] * M
isZero = -1
weight = [[0, chr(ord('A') + i)] for i in range(M)] 

for _ in range(N):
    s = list(input().strip())
    L = len(s)
        
    for i in range(L):
        idx = ord(s[i]) - ord('A')
        if i == 0:
            canBeZero[idx] = False
        weight[idx][0] += 10 ** (L - 1 - i) # A ~ J

minVal = 999_999_999_999 * 50
for i in range(M - 1, -1, -1):
    if canBeZero[i] and weight[i][0] < minVal:
        isZero = i
        minVal = weight[i][0]

weight.sort(key=lambda x : (-x[0], x[1])) 
ans, num = 0, 9
for i in range(M):
    if ord('A') + isZero == ord(weight[i][1]):
        continue
    if weight[i] != 0:
        ans += weight[i][0] * (num)
        num -= 1

print(ans)