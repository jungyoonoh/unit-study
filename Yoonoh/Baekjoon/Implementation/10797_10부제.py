# 10797번 10부제 (Implementation) 
# https://www.acmicpc.net/problem/10797

n = int(input())
car = list(map(int, input().split()))
cnt = 0
for i in range(len(car)):
    if car[i] == n:
        cnt += 1
print(cnt)