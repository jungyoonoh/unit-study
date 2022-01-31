# 백준 1764 듣보잡

import sys
input = sys.stdin.readline


n, m = map(int, input().split())

a = set()
for i in range(n):
    a.add(input().rstrip())

b = set()
for i in range(m):
    b.add(input().rstrip())

ans = sorted(list(a&b))
print(len(ans))
print(*ans, sep='\n')