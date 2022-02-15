#20220211
#백준(DP) : 9095 1,2,3 더하기
#https://www.acmicpc.net/problem/9095

t = int(input())

for _ in range(t):
  n = int(input())
  dp = [0] * 12
  dp[1], dp[2], dp[3] = 1, 2, 4

  for i in range(4,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

  print(dp[n])
