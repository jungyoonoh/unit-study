#20220227
#백준(완전탐색) : 5568 카드 놓기
#https://www.acmicpc.net/problem/5568

from itertools import permutations
n = int(input())
k = int(input())
card = []
for i in range(n):
  card.append(int(input()))


c = list(permutations(card,k))
c = set(c)
cc = []
for i in c:
  cc.append(''.join(tuple(map(str,i))))
  
cc = set(cc)
print(len(cc))
