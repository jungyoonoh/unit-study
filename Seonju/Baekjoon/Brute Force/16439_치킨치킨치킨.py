# 백준 16439 치킨치킨치킨

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
like = [list(map(int, input().split())) for _ in range(n)]

maxSum = 0
for a, b, c in combinations(range(m), 3):
    tmpSum = 0
    for i in range(n):  # i번 회원의 a, b, c번 치킨 선호도 중 가장 큰 값(→ 만족도)을 tmpSum에 얹어줌
        tmpSum += max(like[i][a], like[i][b], like[i][c])
    maxSum = max(maxSum, tmpSum)

print(maxSum)