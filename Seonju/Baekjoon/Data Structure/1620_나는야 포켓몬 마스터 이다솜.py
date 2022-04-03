# 백준 1620 나는야 포켓몬 마스터 이다솜

import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
dic = {}

for i in range(1, n+1):
    name = input()
    dic[i] = name
    dic[name] = i

for j in range(m):
    ask = input()
    if ask.isdigit():
        print(dic[int(ask)])
    else:
        print(dic[ask])