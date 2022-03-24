# 백준 2294 동전 2

import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 동전종류 n가지로 k원 만들기
coins = set()
for _ in range(n):
    coins.add(int(input()))

dp = [0] * (k+1)  # dp[i]는 i원을 만들기 위해 필요한 동전의 최소 개수
for i in range(1, k+1):
    tmp = []
    for coin in coins:
        if i >= coin and dp[i-coin] != -1:
            tmp.append(dp[i-coin]+1)
    if not tmp:
        dp[i] = -1
    else:
        dp[i] = min(tmp)

print(dp[k])
