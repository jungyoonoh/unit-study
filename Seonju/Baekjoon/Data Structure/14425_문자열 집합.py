# 백준 14425 문자열 집합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()  # list로 만들면 시간 3900ms, set으로 만들면 시간 156ms → s에 중복된 문자열이 없다고 명시한 문제의 경우 set으로 만드는 게 이득
for _ in range(n):
    s.add(input().rstrip())
cnt = 0
for _ in range(m):
    if input().rstrip() in s:
        cnt += 1

print(cnt)