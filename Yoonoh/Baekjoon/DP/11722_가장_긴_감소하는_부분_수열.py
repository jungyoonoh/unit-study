# 11722번 가장 긴 감소하는 부분 수열 (DP) 
# https://www.acmicpc.net/problem/11722

import bisect

N = int(input())
info = list(map(int, input().split()))
info = list(reversed(info))
seq = []
seq.append(info[0])
for i in range(1, N):
    if seq[-1] < info[i]:
        seq.append(info[i])
    else:
        idx = bisect.bisect_left(seq, info[i])
        seq[idx] = info[i]
        
print(len(seq))