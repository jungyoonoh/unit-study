#20220227
#백준(투포인터) : 21921 블로그#https://www.acmicpc.net/problem/21921

import sys
#누적 합
from itertools import accumulate
input = sys.stdin.readline

n, x = map(int,input().split())
s = 0
hap = []
a = list(map(int,input().split()))
b = list(accumulate(a))

for i in range(1,n):
  if (i-x) < 0:
    hap.append(b[i])
  else:
    hap.append(b[i]-b[i-x])
      
if max(hap) != 0:
  print(max(hap))
else:
  print('SAD')
  exit(0)

print(hap.count(max(hap)))
