# 백준 20291 파일 정리

import sys
from collections import defaultdict
input = sys.stdin.readline

dic = defaultdict(int)

for _ in range(int(input())):
    file = input().rstrip().split('.')
    dic[file[1]] += 1

dic = sorted(dic.items())

for i, j in dic:
    print(i, j)