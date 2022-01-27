# 14719번 빗물 (Implementation) 
# https://www.acmicpc.net/problem/14719

H, W = map(int, input().split())
block = list(map(int, input().split()))

stack = []
pivot = -1
ans = 0
for i in range(W):           
    if pivot <= block[i]:
        ans += pivot * len(stack) - sum(stack) 
        pivot = block[i]
        stack.clear()
    else:
        stack.append(block[i])

if len(stack) > 0:
    stack.insert(0, pivot)
    rest = []
    pivot = -1
    for i in range(len(stack) - 1, -1, -1):
        if pivot <= stack[i]:
            ans += pivot * len(rest) - sum(rest) 
            pivot = stack[i]
            rest.clear()
        else:
            rest.append(stack[i])
            
print(ans)