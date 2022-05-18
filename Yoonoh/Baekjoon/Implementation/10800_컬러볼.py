# 10800번 컬러볼 (Implementation) 
# https://www.acmicpc.net/problem/10800

from collections import defaultdict
N = int(input())

ball = []
for i in range(N):
    C, S = map(int, input().split())
    ball.append((S, C, i)) # 크기, 색, 원래 인덱스
    
ball.sort(key=lambda x:(x[0], x[1]))
answer = [0] * N

total = 0
j = 0
dd = defaultdict(int)
for i in range(N):
    while ball[j][0] < ball[i][0]:
        total += ball[j][0]
        dd[ball[j][1]] += ball[j][0]
        j += 1
    answer[ball[i][2]] = total - dd[ball[i][1]]

print(*answer)