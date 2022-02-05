# 백준 9375 패션왕 신해빈

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    clothes = dict()
    for _ in range(int(input())):
        name, kind = input().split()
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1

    ans = 1
    for i in clothes.keys():
        ans *= (clothes[i] + 1)
    print(ans - 1)
