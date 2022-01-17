# 백준 15787 기차가 어둠을 헤치고 은하수를

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = [[0 for _ in range(20)] for _ in range(n)]
state = []

for _ in range(m):
    a = list(map(int, input().split()))

    if a[0] == 1:
        train[a[1] - 1][a[2] - 1] = 1
    elif a[0] == 2:
        train[a[1] - 1][a[2] - 1] = 0
    elif a[0] == 3:
        for j in range(19, 0, -1):
            train[a[1] - 1][j] = train[a[1] - 1][j - 1]
        train[a[1] - 1][0] = 0
    elif a[0] == 4:
        for j in range(19):
            train[a[1] - 1][j] = train[a[1] - 1][j + 1]
        train[a[1] - 1][19] = 0

cnt = 0
for i in range(n):
    if train[i] not in state:
        state.append(train[i])
        cnt += 1

print(cnt)
