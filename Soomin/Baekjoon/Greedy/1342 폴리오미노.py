#20220131
#백준(그리디) : 1343 폴리오미노
#https://www.acmicpc.net/problem/1343

n = input()

re = n.replace('XXXX','AAAA')
re = re.replace('XX','BB')

if 'X' in re:
  print(-1)
else:
  print(re)