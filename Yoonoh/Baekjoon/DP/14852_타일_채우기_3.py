# 14852번 타일 채우기 3 (DP) 
# https://www.acmicpc.net/problem/14852

N = int(input())
dp = [0] * (1_000_000)
dp[0] = 1
dp[1] = 2
dp[2] = 7
for i in range(3, N+1):
    dp[i] = (3 * dp[i-1] + dp[i-2] - dp[i-3]) % 1_000_000_007
    
print(dp[N] % 1_000_000_007)