#20220327
#백준(문자열) : 1213 팰린드롬 만들기
#https://www.acmicpc.net/problem/1213

from collections import deque
from collections import Counter

s = list(input())

s.sort()

a = deque()
b = deque()

for i in range(len(s)):
  if i % 2 == 1:
    a.append(s[i])
  else:
    b.appendleft(s[i])

if len(a) != len(b):
  c = list((Counter(b)-Counter(a)).keys())
  b.remove(c[0])
  ab = list(a) + list(c) + list(b)
else:
  ab = list(a)+list(b)
  
if len(ab) == 1:
  print(''.join(ab))
else:
  # print(ab)
  x = ab[:len(ab)//2]
  y = ab[::-1]
  y = y[:len(ab)//2]

  if x == y:
    print(''.join(ab))
  else:
    print("I'm Sorry Hansoo")
