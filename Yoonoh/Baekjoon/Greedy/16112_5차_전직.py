# 16112번 5차 전직 (Greedy) 
# https://www.acmicpc.net/problem/16112

n, k = map(int, input().split())
exp = list(map(int, input().split()))

exp.sort()

active = ans = 0
for i in range(n):
    ans += active * exp[i]
    if active < k:
        active += 1

print(ans)