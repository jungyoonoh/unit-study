# 20300번 서강근육맨 (Greedy) 
# https://www.acmicpc.net/problem/20300

N = int(input())
info = list(map(int, input().split()))
info.sort()
if N % 2 == 1:
    M = info[-1]
    for i in range(N // 2):
        M = max(info[i] + info[N - i - 2], M)
else:
    M = info[0] + info[-1]
    for i in range(1, N // 2 - 1):
        M = max(info[i] + info[N - i - 1], M)
print(M)
