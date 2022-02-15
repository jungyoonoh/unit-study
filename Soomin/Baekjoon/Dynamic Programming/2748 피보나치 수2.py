#20220208
#백준(DP) : 2748
#https://www.acmicpc.net/problem/2748

#dp : 한 번 계산한 문제는 다시 계산하지 않도록 함, 동적계획법

n = int(input())

dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range(2,n+1):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
