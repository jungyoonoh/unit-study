# 백준 1159 농구 경기

import sys
from collections import defaultdict
input = sys.stdin.readline

dic = defaultdict(int)
for _ in range(int(input())):
    name = input().rstrip()
    dic[name[0]] += 1

ans = []
for key, val in dic.items():
    if val > 4:
        ans.append(key)
ans.sort()

print(*ans, sep='') if len(ans) else print("PREDAJA")