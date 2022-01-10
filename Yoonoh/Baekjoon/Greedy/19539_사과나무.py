# 19539번 사과나무 (Greedy) 
# https://www.acmicpc.net/problem/19539

N = int(input())
h = list(map(int, input().split()))
d = o = 0

for i in h:
    d += i // 2
    o += i % 2

if (d - o) % 3 == 0 and d >= o:
    print("YES")
else:
    print("NO")