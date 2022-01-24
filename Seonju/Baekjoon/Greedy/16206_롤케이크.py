# 백준 16206 롤케이크

import sys
input = sys.stdin.readline

n, limit = map(int, input().split())
cake = [int(i) for i in input().split()]

cakeTen = sorted(list(filter(lambda x: x % 10 == 0, cake)))
cakeNotTen = list(filter(lambda x: x % 10 != 0, cake))

cnt = 0

while limit > 0:
    # 10의 배수 케이크가 남아있으면
    if cakeTen:
        if cakeTen[0] // 10 - 1 > limit:
            cnt += limit
            limit = 0
        else:
            cnt += cakeTen[0] // 10
            limit -= (cakeTen[0] // 10 - 1)
        del cakeTen[0]

    # 10의 배수 케이크가 없으면
    elif cakeNotTen:
        if cakeNotTen[0] // 10 > limit:
            cnt += limit
            limit = 0
        else:
            cnt += cakeNotTen[0] // 10
            limit -= cakeNotTen[0] // 10
        del cakeNotTen[0]

    # 모든 케이크를 다 탐색했으면
    else:
        break

print(cnt)