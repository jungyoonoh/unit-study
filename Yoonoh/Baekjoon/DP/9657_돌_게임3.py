# 9657번 돌 게임 3 (DP) 
# https://www.acmicpc.net/problem/9657

N = int(input())
dp = [False] * 1001
dp[1] = dp[3] = dp[4] = True
dp[2] = False
for i in range(5, N+1):
    if dp[i-1] and dp[i-3] and dp[i-4]:
        dp[i] = False
    else:
        dp[i] = True
        
print("SK" if dp[N] == True else "CY")