# 2467번 용액 (TwoPointer) 
# https://www.acmicpc.net/problem/2467

# 산성은 양의 정수
# 알칼리성은 음의 정수

N = int(input())
data = list(map(int, input().split()))

left, right, ansL, ansR = 0, N-1, 0, 0
ans = 2_000_000_001
while left < right:
    total = data[left] + data[right]
    
    if abs(total) < ans:
        ansL, ansR = left, right
        ans = abs(total)
    
    if total > 0:
        right -= 1
    elif total < 0:
        left += 1
    else:
        break

print(data[ansL], data[ansR]) 