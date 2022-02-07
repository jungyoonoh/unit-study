# 백준 1931 회의실 배정

import sys
input = sys.stdin.readline

meet = []
for i in range(int(input())):
    meet.append(tuple(map(int, input().split())))
meet.sort(key=lambda x: (x[1], x[0]))

cnt = 0
last = 0
for start, end in meet:
    if start >= last:
        cnt += 1
        last = end

print(cnt)