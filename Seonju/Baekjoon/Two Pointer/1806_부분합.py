# 백준 1806 부분합

import sys
input = sys.stdin.readline
INF = float('inf')

n, s = map(int, input().split())
nums = list(map(int, input().split()))

end = 0
summary = 0
minLen = INF

for start in range(n):
    while summary < s and end < n:  # end를 가능한 만큼 이동시키기
        summary += nums[end]
        end += 1
    if summary >= s:  # 부분합이 s 이상이면 최소길이 갱신
        minLen = min(minLen, end-start)
    summary -= nums[start]  # start 이동 준비

print(minLen if minLen != INF else 0)
