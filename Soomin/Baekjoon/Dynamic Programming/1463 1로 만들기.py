#20220214
#백준(DP) : 1463 1로 만들기
#https://www.acmicpc.net/problem/1463

n = int(input())

dp = [0 for _ in range(n+1)]

for i in range(2,n+1):
  dp[i] = dp[i-1] + 1
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3]+1)
  if i % 2 == 0: #elif 하면 안됨
    dp[i] = min(dp[i], dp[i//2]+1)
  
print(dp[n])