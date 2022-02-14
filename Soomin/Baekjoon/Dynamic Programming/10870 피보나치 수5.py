#20220213
#백준(DP) : 10870 피보나치 수5
#https://www.acmicpc.net/problem/10870

n = int(input())

dp = [0] * 21
dp[0] = 0
dp[1] = 1

for i in range(2,21):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n])