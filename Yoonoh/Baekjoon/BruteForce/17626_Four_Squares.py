# 17626번 Four Squares (BruteForce) 
# https://www.acmicpc.net/problem/17626

n = int(input())

dp = [0] * 50001
dp[1] = 1

for i in range(2, n+1):
    m = 50001 ** 2
    mul = 1
    while i - mul**2 >= 0:
        m = min(m, dp[i - mul**2])
        mul += 1
    
    dp[i] = m + 1

print(dp[n])