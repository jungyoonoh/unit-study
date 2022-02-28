# 백준 20922 겹치는 건 싫어

import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

dic = defaultdict(int)
size, ans, end = 0, 0, 0

for start in range(n):
    while end < n and dic[lst[end]] < k:
        dic[lst[end]] += 1
        size += 1
        end += 1
    if ans < size:
        ans = size
    size -= 1
    dic[lst[start]] -= 1

print(ans)