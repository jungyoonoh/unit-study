# 24393번 조커 찾기 (Implementation) 
# https://www.acmicpc.net/problem/24393

import sys
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
jokerDir = -1 # L, R -1, 1
joker = 1 # 첫 층
for i in range(N):
    total = 0
    flag = False
    for j in range(len(info[i])):
        if j % 2 == 0:
            if jokerDir == 1 and not flag:
                if joker - info[i][j] <= 0:
                    joker = total + joker
                    flag = True
                else:
                    joker -= info[i][j]
        else:
            if jokerDir == -1 and not flag:
                if joker - info[i][j] <= 0:
                    joker = total + joker
                    flag = True
                else:
                    joker -= info[i][j]    
        total += info[i][j]

    if i == N-1:
        break
    
    if joker > 13:
        jokerDir = 1
        joker -= 13
    else:
        jokerDir = -1

print(joker)