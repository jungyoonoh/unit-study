# 백준 2230 수 고르기

n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort()

left, right = 0, 0
ans = float('inf')

while left < n and right < n:
    diff = data[right] - data[left]
    if diff < m:
        right += 1
    else:
        ans = min(ans, diff)
        left += 1

print(ans)

