# 백준 20300 서강근육맨

import sys
input = sys.stdin.readline

n = int(input())
loss = [int(i) for i in input().split()]
loss.sort()

if n % 2 != 0:
    mx = loss[n-1]
    for i in range(n // 2):
        mx = max(mx, loss[i] + loss[n-i-2])
else:
    mx = 0
    for i in range(n // 2):
        mx = max(mx, loss[i] + loss[n-i-1])

print(mx)