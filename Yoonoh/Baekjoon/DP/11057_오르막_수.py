# 11057번 오르막 수 (DP) 
# https://www.acmicpc.net/problem/11057d

N = int(input())

digit = [1] * 10
dp = [0] * 1001
for i in range(N):
    dp[i] = sum(digit) % 10007
    total = 0
    for i in range(9, -1, -1):
        total += digit[i]
        digit[i] = total

print(dp[N-1])