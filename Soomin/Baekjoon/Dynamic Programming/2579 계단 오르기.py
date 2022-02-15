#20220212
#백준(DP) : 2579 계단 오르기
#https://www.acmicpc.net/problem/2579

n = int(input())
stair = [int(input()) for _ in range(n)]
# print(stair)
dp = [0] * n
dp[0] = stair[0]

if n>1:
  dp[1] = max(stair[0]+stair[1], stair[1])
if n>2:
  dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])

  for i in range(3,n):
    dp[i] = max(dp[i-2]+stair[i], dp[i-3] + stair[i-1]+stair[i])

print(dp[n-1])
