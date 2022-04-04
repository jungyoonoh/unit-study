# 백준 10987 모음의 개수

import sys
input = sys.stdin.readline

cnt = 0
for i in input().rstrip():
    if i in 'aeiou':
        cnt += 1
print(cnt)