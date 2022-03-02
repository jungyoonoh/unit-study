# 2293번 동전1 (DP) 
# https://www.acmicpc.net/problem/2293

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)
dp = [0 for _ in range(k+1)]
dp[0] = 1
for c in coin:
    for i in range(c, k+1):
        if i - c >= 0:
            dp[i] += dp[i-c]

print(dp[k])