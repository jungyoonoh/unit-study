# 2480번 주사위 세개 (Implementation) 
# https://www.acmicpc.net/problem/2480

dice = [0, 0, 0, 0, 0, 0, 0]
reword = [0, 0, 1000, 10000]
mul = [0, 100, 100, 1000]
a, b, c = map(int, input().split())
dice[a] += 1
dice[b] += 1
dice[c] += 1

m = max(dice)
t = 0
for i in range(1, 7):
    if m == dice[i]:
        t = i

print(reword[m] + (t * mul[m]))