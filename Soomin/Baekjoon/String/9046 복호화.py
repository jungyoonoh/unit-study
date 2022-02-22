#20220220
#백준(문자열) : 9046 복호화
#https://www.acmicpc.net/problem/9046

n = int(input())

for _ in range(n):
  s = list(input().replace(' ',''))

  c = []
  for i in s:
    c.append(s.count(i))
  
  m = c.index(max(c))

  a = []
  for j in range(m,len(c)):
    if c[j] >= c[m]:
      a.append(s[j])
  
  a = set(a)
  
  if len(a) == 1:
    print(s[c.index(max(c))])
  else:
    print("?")

