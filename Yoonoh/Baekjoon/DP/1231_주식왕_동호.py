# 1231번 주식왕 동호 (DP) 
# https://www.acmicpc.net/problem/1231

C, D, M = map(int, input().split())
stockPrice = []

for i in range(C):
    stockPrice.append(list(map(int, input().split())))

for day in range(1, D): # D일간 매매
    dp = [0] * (M+1) # 각 일별로 벌 수 있는 최대 금액 구하기
    for stock in range(C):
        for budget in range(1, M+1):
            if (budget - stockPrice[stock][day - 1] < 0): # 어제 살 수 없었다면
                continue
            dp[budget] = max(dp[budget], dp[budget - stockPrice[stock][day - 1]] + stockPrice[stock][day] - stockPrice[stock][day - 1])
    
    M += dp[budget] # 그날의 매매 결과로 자본증가

print(M)