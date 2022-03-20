# 백준 17212 달나라 토끼를 위한 구매대금 지불 도우미

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)  # dp[i]는 i원을 만들 수 있는 동전의 최소개수

for i in range(1, n+1):
    tmp = []
    for coin in [1, 2, 5, 7]:
        if i >= coin:
            tmp.append(dp[i-coin])
    dp[i] = min(tmp) + 1

print(dp[n])
