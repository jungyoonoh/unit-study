# 17404번 RGB거리 2 (DP) 
# https://www.acmicpc.net/problem/17404

import sys
input = sys.stdin.readline

MAX = 2147483648
N = int(input())
cost = []
dpRed = [0] * N
ans = MAX
for i in range(N):
    cost.append(list(map(int, input().split())))

for i in range(3): # 맨앞을 어떤 색으로 할지
    dp = [[MAX, MAX, MAX] for _ in range(N)]
    dp[0][i] = cost[0][i]
    
    for j in range(1, N):
        dp[j][0] = cost[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = cost[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = cost[j][2] + min(dp[j-1][0], dp[j-1][1])\
    
    for j in range(3):
        if i == j:
            continue # 처음과 끝은 같으면 안된다
        ans = min(ans, dp[-1][j])

print(ans)