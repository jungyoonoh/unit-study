# 22869번 징검다리 건너기 (Small) (DP) 
# https://www.acmicpc.net/problem/22869

N, K = map(int, input().split())
rock = list(map(int, input().split()))
dp = [99999999] * N # 0 ~ N-1
dp[0] = 0

for i in range(N - 1):
    if dp[i] > K:
        continue
    
    for j in range(i + 1, N):
        dp[j] = min((j - i) * (1 + abs(rock[j] - rock[i])), dp[j])

print("YES" if dp[N - 1] <= K else "NO")