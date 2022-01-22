#20220122
#백준(그리디) : 16208 귀찮음
#https://www.acmicpc.net/problem/16208

n = int(input())
a = list(map(int,input().split()))

have = sum(a)
a.sort(reverse=True)
cost = 0
for i in a:
  have -= i
  cost += i * have

print(cost)