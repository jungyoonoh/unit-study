# 2473번 세 용액 (TwoPointer) 
# https://www.acmicpc.net/problem/2473

N = int(input())
data = list(map(int, input().split()))

data.sort()
minVal = 3_000_000_001
ans = [0, 0, 0]
flag = False
for i in range(N-2):
    left, right = i+1, N-1
    
    while left < right:
        total = data[left] + data[right] + data[i]
        if abs(total) < minVal:
            minVal = abs(total)
            ans[0], ans[1], ans[2] = data[i], data[left], data[right]
        
        if total > 0:
            right -= 1
        elif total < 0:
            left += 1
        else:
            flag = True
            break

    if flag:
        break

print(*ans)