# 백준 9996 한국이 그리울 땐 서버에 접속하지

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
pattern = input()
star = pattern.index('*')
before, after = pattern[:star], pattern[star+1:]

for _ in range(n):
    name = input()

    if before in name and after in name:
        former = name.index(before)
        later = name.index(after)

        if former == 0 and former+len(before) <= later and name[::-1].index(after[::-1]) == 0:
            print('DA')
            continue

    print('NE')