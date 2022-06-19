# 11478번 서로 다른 부분 문자열의 개수 (String) 
# https://www.acmicpc.net/problem/11478

S = list(input().strip())
pool = set()
for i in range(1, len(S) + 1):
    for j in range(len(S)):
        pool.add("".join(S[j:j+i]))

print(len(pool))