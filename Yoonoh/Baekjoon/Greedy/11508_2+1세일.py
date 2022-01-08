# 11508번 2+1 세일 (Greedy) 
# https://www.acmicpc.net/problem/11508

N = int(input())

data = []
for i in range(N):
    data.append(int(input()))
    
data.sort(reverse=True)
ans = 0
for i in range(N):
    if i % 3 == 2:
        continue
    ans += data[i]
    
print(ans)