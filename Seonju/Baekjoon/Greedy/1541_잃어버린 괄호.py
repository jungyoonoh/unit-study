# 백준 1541 잃어버린 괄호

import sys
input = sys.stdin.readline

data = input().rstrip().split('-')
ans = 0

for i in data[0].split('+'):
    ans += int(i)

for i in data[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)