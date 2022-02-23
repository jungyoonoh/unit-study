import sys
from bisect import bisect_left
input = sys.stdin.readline

m, n, l = map(int, input().split())
shoot = list(map(int, input().split()))
shoot.sort()

cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    if y <= l:
        idx = bisect_left(shoot, x)
        for k in [idx-1, idx, idx+1]:
            if k < 0 or k >= m:
                continue
            if abs(shoot[k] - x) + y <= l:
                cnt += 1
                break
print(cnt)