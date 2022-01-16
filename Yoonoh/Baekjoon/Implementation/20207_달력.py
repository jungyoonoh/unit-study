# 20207번 달력 (Implementation) 
# https://www.acmicpc.net/problem/20207

import itertools

N = int(input())

schedule = [0] * 367 # 1 ~ 365 + 2

for i in range(N):
    S, E = map(int, input().split())
    schedule[S] += 1
    schedule[E+1] -= 1

accSchedule = list(itertools.accumulate(schedule))
start = end = 1
switchFlag = False
ans = 0
for i in range(1, 367):
    if not switchFlag and accSchedule[i] > 0:
        start = i
        switchFlag = True
        continue
    
    if switchFlag and accSchedule[i] <= 0:
        end = i
        M = max(accSchedule[start:end])
        W = end - start
        ans += M * W
        switchFlag = False

print(ans)