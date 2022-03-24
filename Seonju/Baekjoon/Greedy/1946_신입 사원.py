# 백준 1946 신입 사원

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    people = [list(map(int, input().split())) for _ in range(n)]
    people.sort()

    cnt = 0
    minimum = n+1
    for person in people:
        if person[1] < minimum:
            cnt += 1
            minimum = person[1]
    print(cnt)
