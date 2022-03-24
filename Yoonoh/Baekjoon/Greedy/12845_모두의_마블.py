# 12845번 모두의 마블 (Greedy) 
# https://www.acmicpc.net/problem/12845

N = int(input())
level = list(map(int, input().split()))
total = 0
index = level.index(max(level))
for i in range(index - 1, -1, -1):
    total += level[index] + level[i]

for i in range(index + 1, N):
    total += level[index] + level[i]

print(total)
