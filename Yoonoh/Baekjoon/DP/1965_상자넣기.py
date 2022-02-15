# 1965번 상자넣기 (DP) 
# https://www.acmicpc.net/problem/1965

import bisect

N = int(input())
box = list(map(int, input().split()))
ans = []
ans.append(box[0])
for i in range(1, N):
    if ans[-1] < box[i]:
        ans.append(box[i])
    else:
        idx = bisect.bisect_left(ans, box[i])
        ans[idx] = box[i]

print(len(ans))