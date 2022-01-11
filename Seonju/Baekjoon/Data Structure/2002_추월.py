# 백준 2002 추월

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
seq_in = deque(input().strip() for _ in range(n))
seq_out = deque(input().strip() for _ in range(n))

cnt = 0

for _ in range(n):
    out = seq_out.popleft()
    if out != seq_in[0]:
        seq_in.remove(out)
        cnt += 1
    else:
        seq_in.popleft()

print(cnt)