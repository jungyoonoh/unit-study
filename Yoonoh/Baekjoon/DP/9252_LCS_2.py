# 9252번 LCS 2 (DP) 
# https://www.acmicpc.net/problem/9252

s1 = input().strip()
s2 = input().strip()

L1 = len(s1)
L2 = len(s2)

dp = [[""] * (L2 + 1) for _ in range(L1 + 1)]

for i in range(1, L1 + 1):
    for j in range(1, L2 + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + s1[i-1]
        else:
            if len(dp[i][j-1]) < len(dp[i-1][j]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))

if len(dp[-1][-1]):
    print(dp[-1][-1])