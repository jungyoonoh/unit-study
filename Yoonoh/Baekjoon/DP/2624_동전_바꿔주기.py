# 2624번 동전 바꿔주기 (DP) 
# https://www.acmicpc.net/problem/2624

T = int(input())
k = int(input())

info = [(0, 0)]
dp = [[0 for _ in range(T+1)] for _ in range(k+1)]
for i in range(k):
    p, n = map(int, input().split())
    info.append((p, n))
info.sort()
dp[0][0] = 1
for i in range(1, k+1): # i번째 동전까지만 이용해서
    coin, cnt = info[i][0], info[i][1]
    for j in range(T+1): # 0원부터 T원까지 만들어보기
        dp[i][j] = dp[i-1][j] # i번째 동전을 사용하지 않는 값으로 초기화
        for n in range(1, cnt + 1): # 제한된 개수를 이용해서
            if j - n * coin >= 0: # 현재 동전을 쓰지 않고 만들었던 경우의 수 중에, 동전 금액 * 개수만큼 이전 금액의 경우의 수 추가
                dp[i][j] += dp[i-1][j - n * coin]
            else:
                break
            
print(dp[k][T])