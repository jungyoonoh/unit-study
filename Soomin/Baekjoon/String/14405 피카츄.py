#20220403
#백준(문자열) : 14405 피카츄
#https://www.acmicpc.net/problem/14405

p = ['pi','ka','chu']

s = input()

for i in p:
  if i in s:
    s = s.replace(i, '*')

tag = 1

for i in s:
  if i != '*':
    tag = 0

if tag == 1:
  print("YES")
else:
  print("NO")