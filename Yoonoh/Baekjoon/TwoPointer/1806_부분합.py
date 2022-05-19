# 1806번 부분합 (TwoPointer) 
# https://www.acmicpc.net/problem/1806

N, S = map(int, input().split())
data = list(map(int, input().split()))

end = 0
total = data[0]
ans = 100001
for start in range(N):
    while end < N - 1:
        if total < S:
            end += 1
            total += data[end]
        else:
            break
    
    if total >= S:
        ans = min(ans, end - start + 1)
        total -= data[start]

print(ans if ans != 100001 else 0)