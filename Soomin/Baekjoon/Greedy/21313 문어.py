#20220120
#백준(그리디) : 21313 문어
#https://www.acmicpc.net/problem/21313

n = int(input())

if n%2 == 0:
  print('1 2 '*(n//2))
else:
  print('1 2 '*(n//2)+'3')