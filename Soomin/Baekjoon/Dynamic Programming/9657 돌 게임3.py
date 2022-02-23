#20220215
#백준(DP) : 9657 돌 게임3
#https://www.acmicpc.net/problem/9657

n = int(input())

dp = [0] * 1001

dp[1] = dp[3] = dp[4] = 1
dp[2] = 0

for i in range(5, n+1):
  if dp[i-1] and dp[i-3] and dp[i-4]:
    dp[i] = 0
  else:
    dp[i] = 1

if dp[n] == 1:
  print("SK")
else:
  print("CY")