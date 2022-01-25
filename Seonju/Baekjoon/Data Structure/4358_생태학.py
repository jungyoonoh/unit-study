# 백준 4358 생태학

import sys
from collections import Counter
input = sys.stdin.readline

trees = []
cnt = 0

while True:
    name = input().rstrip()
    if not name:
        break
    trees.append(name)
    cnt += 1

trees = sorted(Counter(trees).items())

for i in range(len(trees)):
    print(trees[i][0], "{:.4f}".format(trees[i][1]/cnt*100))
