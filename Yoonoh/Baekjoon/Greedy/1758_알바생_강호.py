# 1758번 알바생 강호 (Greedy) 
# https://www.acmicpc.net/problem/1758

N = int(input())

tips = []
for i in range(N):
    tips.append(int(input()))

tips.sort(reverse=True)

ans = 0
for i in range(N):
    if tips[i] - i > 0:
        ans += tips[i] - i

print(ans)