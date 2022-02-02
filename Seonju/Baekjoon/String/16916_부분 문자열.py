# 백준 16916 부분 문자열

import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

if p in s:
    print(1)
else:
    print(0)