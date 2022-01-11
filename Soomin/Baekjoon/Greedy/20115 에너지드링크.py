#20220110
#백준(그리디) : 20115 에너지드링크
#https://www.acmicpc.net/problem/20115

n = int(input())
d = list(map(int,input().split()))

d.sort(reverse=True)
e_max = 0

for i in range(n-1):
  e_max = d[0] + (d[-1] / 2)
  d[0] = e_max
  del d[-1]

print("%g" %e_max)
