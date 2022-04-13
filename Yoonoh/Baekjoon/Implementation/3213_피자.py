# 3213번 피자 (Implementation) 
# https://www.acmicpc.net/problem/3213

N = int(input())
pizza = [0, 0, 0]
for i in range(N):
    a, b = map(int, input().split('/'))
    if b == 2:
        pizza[1] += 1
    elif a == 3:
        pizza[2] += 1
    else:
        pizza[0] += 1

ans = 0
ans += pizza[1] // 2
pizza[1] -= (pizza[1] // 2) * 2

temp = min(pizza[0], pizza[2])
ans += temp
pizza[0] -= temp
pizza[2] -= temp

temp = min(pizza[0], pizza[1])            
ans += temp
pizza[0] -= temp
pizza[1] -= temp

ans += pizza[0] // 4
pizza[0] -= (pizza[0] // 4) * 4
if pizza[0] > 0:
    ans += 1

ans += pizza[1] + pizza[2]
print(ans)