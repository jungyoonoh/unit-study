# 7579번 앱 (Greedy) 
# https://www.acmicpc.net/problem/7579

N, M = map(int, input().split()) # 앱 수, 확보해야할 메모리
m = [0] + list(map(int, input().split())) # 정리되는 메모리 바이트
c = [0] + list(map(int, input().split())) # 정리 당 비용
dp = [[0 for _ in range(sum(c) + 1)] for _ in range(N+1)]
r = sum(c) 
minVal = sum(c) # 모든 앱을 꺼야하는 경우가 최악의 케이스

for i in range(1, N+1):
    byte, cost = m[i], c[i] # i번째 앱을 끌 경우 확보되는 메모리와 이에 대한 비용
    
    for j in range(1, r+1):
        if j < cost: # 현재 코스트로 작업을 수행할 수 없다면
            dp[i][j] = dp[i-1][j] # 이전 상태 그대로
        else:
            dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j]) # 앱을 끔으로서 메모리 확보가 더 큰지, 이번 cost 선택 안한것이 더 큰지
        
        if dp[i][j] >= M: # 조건 만족시 cost 갱신
            minVal = min(minVal, j)

print(minVal)