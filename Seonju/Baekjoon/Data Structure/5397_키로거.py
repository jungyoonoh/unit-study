# 백준 5397 키로거

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    pw = input().rstrip()
    left, right = [], deque()

    for now in pw:
        if now == '<' and left:
            right.appendleft(left.pop())
        elif now == '>' and right:
            left.append(right.popleft())
        elif now == '-' and left:
            left.pop()
        elif now.isalnum():
            left.append(now)

    print(''.join(map(str, left+list(right))))
