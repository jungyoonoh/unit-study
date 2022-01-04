# 백준 2841 외계인의 기타 연주

import sys
input = sys.stdin.readline

n, p = map(int, input().split())
lines = [[] for _ in range(7)]
cnt = 0

for _ in range(n):
    line, fret = map(int, input().split())
    line = lines[line - 1]

    while line and fret < line[-1]:
        line.pop()
        cnt += 1

    if not line or fret > line[-1]:
        line.append(fret)
        cnt += 1

print(cnt)