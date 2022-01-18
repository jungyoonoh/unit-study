#20220111
#백준(그리디) : 1758 알바생강호
#https://www.acmicpc.net/problem/1758
n = int(input())
c = []

for i in range(n):
  c.append(int(input()))

c.sort(reverse=True)

tip = 0

for i in range(n):
  if c[i]-i < 0:
    tip += 0
  else:
    tip += c[i]-i

print(tip)