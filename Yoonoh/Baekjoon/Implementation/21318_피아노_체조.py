# 21318번 피아노 체조 (Implementation) 
# https://www.acmicpc.net/problem/21318

import sys
input = sys.stdin.readline

N = int(input())
level = list(map(int, input().split()))
miss = [0] * N
for i in range(1, N):
    if level[i-1] > level[i]:
        miss[i] = miss[i-1] + 1 # 실수
    else:
        miss[i] = miss[i-1]

Q = int(input())
for _ in range(Q):
    start, end = map(int, input().split())
    print(miss[end-1] - miss[start-1])