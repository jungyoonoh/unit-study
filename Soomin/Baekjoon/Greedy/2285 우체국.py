#20220220
#백준(그리디) : 2285 우체국
#https://www.acmicpc.net/problem/2285

n = int(input())
v = []
people = 0
for _ in range(n):
  x, a = map(int,input().split())
  v.append([x,a])
  people += a
v.sort()

post = 0

for i in range(n):
  post += v[i][1]

  if post >= (people/2):
    print(v[i][0])
    exit(0)

