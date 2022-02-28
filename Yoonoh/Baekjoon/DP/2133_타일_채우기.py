# 2133번 타일 채우기 (DP) 
# https://www.acmicpc.net/problem/2133

dp = [0] * 31 # 0 ~ 29
dp[0] = 1
dp[2] = 3
for i in range(4, 31, 2):
    dp[i] = dp[i-2] * 3
    for j in range(4, i+1, 2):
        dp[i] += dp[i-j] * 2
            
print(dp[int(input())])