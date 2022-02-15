# 14002번 가장 긴 증가하는 부분 수열 4 (DP) 
# https://www.acmicpc.net/problem/14002

import bisect

N = int(input())
info = list(map(int, input().split()))
seq = []
temp = []
seq.append(info[0])
temp.append((0, info[0]))
for i in range(1, N):
    if seq[-1] < info[i]:
        seq.append(info[i])
        temp.append((len(seq) - 1, info[i]))
    else:
        idx = bisect.bisect_left(seq, info[i])
        seq[idx] = info[i]
        temp.append((idx, info[i]))

last = len(seq) - 1
ans = []
for i in range(N-1, -1, -1):
    if temp[i][0] == last:
        ans.append(temp[i][1])
        last -= 1
        
print(len(ans))
print(*reversed(ans))