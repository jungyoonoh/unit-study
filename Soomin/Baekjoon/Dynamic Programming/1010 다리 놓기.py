#20220209
#백준(DP) : 1010 다리 놓기
#https://www.acmicpc.net/problem/1010

num = int(input())

for _ in range(num):
  
  dp = [[0] * 31 for _ in range(31)]

  #서쪽 1번 - 동쪽 1번
  for i in range(31):
    dp[1][i] = i

  #나머지
  for i in range(2,31):
    for j in range(2,31):
      dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
      
  n, m = map(int, input().split())
  print(dp[n][m])