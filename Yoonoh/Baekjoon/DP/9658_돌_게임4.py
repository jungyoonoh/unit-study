# 9658번 돌 게임 4 (DP) 
# https://www.acmicpc.net/problem/9658

N = int(input())
dp = [False] * 1001
dp[1] = dp[3] = False
dp[2] = dp[4] = True
for i in range(5, N+1):
    if not dp[i-1] or not dp[i-3] or not dp[i-4]:
        dp[i] = True
    else:
        dp[i] = False
        
print("SK" if dp[N] == True else "CY")