# 백준 19638 센티와 마법의 뿅망치

import sys, heapq
input = sys.stdin.readline

n, h, t = map(int, input().split())
giants = [-int(input()) for _ in range(n)]
heapq.heapify(giants)
cnt = 0

for i in range(t):
    if -giants[0] == 1 or -giants[0] < h:
        break
    else:
        heapq.heapreplace(giants, -(-giants[0] // 2))
        cnt += 1

if -giants[0] >= h:
    print('NO', -giants[0], sep='\n')
else:
    print('YES', cnt, sep='\n')