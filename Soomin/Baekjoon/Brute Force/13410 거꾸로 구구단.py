#20220303
#백준(완전탐색) : 13410 거꾸로 구구단
#https://www.acmicpc.net/problem/13410

n, k = map(int,input().split())

g = []

for i in range(1,k+1):
  re = list(str(n*i))
  r = []
  for j in range(len(re)-1,-1,-1):
    r.append(re[j])
  rr = ''.join(r)
  g.append(rr)

g = list(map(int,g))
g.sort(reverse=True)

print(g[0])

