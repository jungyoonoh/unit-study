# 1365번 꼬인 전깃줄 (BinarySearch) 
# https://www.acmicpc.net/problem/1365

import bisect

N = int(input())
data = list(map(int, input().split()))
cnt = 0
ans = []
for i in data:
    idx = bisect.bisect_left(ans, i)
    if idx == cnt:
        ans.append(i)
        cnt += 1
    else:
        ans[idx] = i

print(N - cnt)