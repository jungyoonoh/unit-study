# 2568번 전깃줄 2 (BinarySearch) 
# https://www.acmicpc.net/problem/2568

import bisect
import sys
input = sys.stdin.readline
N = int(input())

mapper = dict()
for i in range(N):
    A, B = map(int, input().split())
    mapper[B] = A # B에 연결된 A 번호

temp = sorted(mapper.keys())
data = []
for i in temp:
    data.append(mapper[i])
cnt = 0
seq = []
result = []
for b in data:
    idx = bisect.bisect_left(seq, b)
    if idx == cnt:
        seq.append(b)
        cnt += 1
    else:
        seq[idx] = b
    result.append(idx)

print(N - cnt)
backtrace = []
L = len(seq) - 1
for i in range(N - 1, -1, -1):
    if result[i] == L:
        backtrace.append(data[i])
        L -= 1

for i in backtrace:
    data.remove(i)
data.sort()
for i in data:
    print(i)