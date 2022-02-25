#20220225
#백준(완전탐색) : 2798 블랙잭
#https://www.acmicpc.net/problem/2798

from itertools import combinations

n,m = map(int,input().split())
card = list(map(int,input().split()))

c = list(combinations(card,3))
cc = []
for i in c:
  cc.append(sum(i))
cc.sort()
for i in cc:
  # print(i)
  if i <= m:
    ans = i
  else:
    break

print(ans)
