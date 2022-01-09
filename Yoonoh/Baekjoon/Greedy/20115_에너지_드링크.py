# 20115번 에너지 드링크 (Greedy) 
# https://www.acmicpc.net/problem/20115

N = int(input())
amount = list(map(int, input().split()))

amount.sort()
ans = 0
for i in range(N-1):
    ans += amount[i] / 2

ans += amount[-1]

# 소숫점 아래 의미 없는 0을 제거하는 포맷
print('{:g}'.format(ans))