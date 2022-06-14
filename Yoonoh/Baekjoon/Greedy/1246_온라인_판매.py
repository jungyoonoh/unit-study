# 1246번 온라인 판매 (Greedy) 
# https://www.acmicpc.net/problem/1246

N, M = map(int, input().split())

data = []
for i in range(M):
    data.append(int(input()))

data.sort()
maxIncome = 0
maxPrice = 0
for i in range(M):
    sellCnt = M - i if M - i <= N else N
    income = sellCnt * data[i]
    if maxIncome < income:
        maxIncome = income
        maxPrice = data[i]

print(maxPrice, maxIncome)