# 4358번 생태학 (String) 
# https://www.acmicpc.net/problem/4358

from collections import defaultdict
import sys

input = sys.stdin.readline
dd = defaultdict(int)
cnt = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    dd[tree] += 1
    cnt += 1

data = list(dd.keys())
data.sort()

for tree in data:
    print('%s %.4f' %(tree, (dd[tree] / cnt) * 100))