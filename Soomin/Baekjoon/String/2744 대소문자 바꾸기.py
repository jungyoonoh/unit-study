#20220323
#백준(문자열) : 2744 대소문자 바꾸기
#https://www.acmicpc.net/problem/2744

s = list(input())
n = []
for i in s:
  if i.isupper() == True:
    n.append(i.lower())
  else:
    n.append(i.upper())

print(''.join(n))