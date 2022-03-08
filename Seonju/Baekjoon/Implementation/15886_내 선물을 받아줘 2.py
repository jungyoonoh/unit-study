# 백준 15886 내 선물을 받아줘 2

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
pos = list(input())

cnt = 0
for i in range(n - 1):
    if pos[i] + pos[i + 1] == 'EW':
        cnt += 1

print(cnt)