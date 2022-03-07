# 백준 2470 두 용액

import sys
input = sys.stdin.readline

n = int(input())
liquid = sorted(list(map(int, input().split())))

ans = 10e9 + 1
ans_list = []

start, end = 0, n - 1

while start < end:
    val = liquid[start] + liquid[end]
    if abs(val) < abs(ans):
        ans = val
        ans_list = [liquid[start], liquid[end]]
    if val < 0:
        start += 1
    else:
        end -= 1

print(' '.join(map(str, ans_list)))
