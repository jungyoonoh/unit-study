# 19941번 햄버거 분배 (Greedy) 
# https://www.acmicpc.net/problem/19941

N, K = map(int, input().split())
S = list(input())
info = [1 if S[i] == 'H' else 0 for i in range(N)]

for i in range(N):
    if info[i] == 1:
        start = i - K if i - K >= 0 else 0
        end = i + K + 1 if i + K + 1 <= N else N
        for j in range(start, end):
            if info[j] == 0:
                info[j] = 2
                break

print(info.count(2))