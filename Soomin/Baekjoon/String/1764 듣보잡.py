#20220217
#백준(문자열) : 1764 듣보잡
#https://www.acmicpc.net/problem/1764

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

nl = set()
for _ in range(n):
  nl.add(input().strip())

ml = set()
for _ in range(m):
  ml.add(input().strip())

#set과 &(교집합) 이용하면 시간초과 없음
nm = sorted(list(nl & ml))

#시간초과
# for i in nl:
#   # print(":",i)
#   if i in ml:
#     nm.append(i)
# # print(nm)
# nm.sort()
print(len(nm))
for k in nm:
  print(k)
