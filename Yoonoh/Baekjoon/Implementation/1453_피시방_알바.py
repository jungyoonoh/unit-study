# 1453번 피시방 알바 (Implementation) 
# https://www.acmicpc.net/problem/1453

N = int(input())
data = list(map(int, input().split()))
pool = set()
ans = 0
for num in data:
    if num in pool:
        ans += 1
    else:
        pool.add(num)

print(ans)