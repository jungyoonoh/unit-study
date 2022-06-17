# 5582번 공통 부분 문자열 (String) 
# https://www.acmicpc.net/problem/5582

s1 = input().strip()
s2 = input().strip()

L1 = len(s1)
L2 = len(s2)
lcs = [[0 for _ in range(L2 + 1)] for _ in range(L1 + 1)]
ans = 0
for i in range(1, L1 + 1):
    for j in range(1, L2 + 1):
        if s1[i-1] == s2[j-1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
            ans = max(ans, lcs[i][j])
print(ans)