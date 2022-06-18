# 2559번 수열 (TwoPointer) 
# https://www.acmicpc.net/problem/2559

import itertools

N, K = map(int, input().split())
data = list(map(int, input().split()))
accSum = list(itertools.accumulate(data))
ans = accSum[K - 1]
print(accSum)
for start in range(N - K):
    ans = max(ans, accSum[start + K] - accSum[start])

print(ans)