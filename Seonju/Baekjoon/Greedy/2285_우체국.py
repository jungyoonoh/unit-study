# 백준 2285 우체국

import sys
input = sys.stdin.readline

town = []
people = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    town.append((a, b))
    people += b
town.sort()

cnt = 0
for loc, p in town:
    cnt += p
    if cnt >= people / 2:
        print(loc)
        break