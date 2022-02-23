#20220216
#백준(문자열) : 16171 나는 친구가 적다(small)
#https://www.acmicpc.net/problem/16171

s = list(input())
search = input()
alpha = []
for i in s:
  if i.isalpha() == True:
    alpha.append(i)

alpha = ''.join(alpha)

if search in alpha:
  print(1)
else:
  print(0)