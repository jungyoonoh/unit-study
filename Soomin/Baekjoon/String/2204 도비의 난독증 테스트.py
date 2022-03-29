#20220329
#백준(문자열) : 2204 도비의 난독증 테스트
#https://www.acmicpc.net/problem/2204

while True:
  n = int(input())

  if n == 0:
    exit(0)
  s = []
  for i in range(n):
    s.append([input(),i])

  ss =[]

  for i in range(n):
    ss.append([s[i][0].lower(),s[i][1]])

  ss.sort()
  
  
  print(s[ss[0][1]][0])

