# 2285번 우체국 (Greedy) 
# https://www.acmicpc.net/problem/2285

import itertools, sys

input = sys.stdin.readline
N = int(input())
info = []

for _ in range(N):
    town, peopleNum = map(int, input().split())
    info.append((town, peopleNum))

info.sort()
val = list(zip(*info))
ac = list(itertools.accumulate(val[1]))
l, r = 0, len(ac) - 1
townNum = 1_000_000_000
while l <= r:
    mid = (l+r) // 2
    ls = ac[mid]
    rs = ac[-1] - ac[mid]
    
    if ls >= rs:
        r = mid - 1
    else:
        l = mid + 1
        
print(info[r+1][0]) # 마을이 음수에 위치할 수 있음