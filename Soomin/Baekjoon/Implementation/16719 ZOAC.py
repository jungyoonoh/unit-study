#20220124
#백준(구현) : 16719 ZOAC
#https://www.acmicpc.net/problem/16719

#메모리초과

from itertools import combinations
a = list(input())

for i in range(len(a)):
  if i == 0:
    print(min(a))
  else:
    s = list(combinations(a,i+1))
    s.sort()
    print("".join(s[0]))
