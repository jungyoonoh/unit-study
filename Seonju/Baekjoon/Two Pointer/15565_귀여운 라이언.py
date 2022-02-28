# 백준 15565 귀여운 라이언

import sys
input = sys.stdin.readline
INF = float('inf')

n, k = map(int, input().split())
doll = list(map(int, input().split()))

size, cnt, end = 0, 0, 0
ans = INF

for start in range(n):
    while cnt < k and end < n:
        size += 1
        if doll[end] == 1:
            cnt += 1
        end += 1

    if cnt == k and ans > size:
        ans = size

    if doll[start] == 1:
        cnt -= 1
    size -= 1

print(ans if ans != INF else -1)