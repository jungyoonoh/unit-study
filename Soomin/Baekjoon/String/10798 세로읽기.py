#20220128
#백준(문자열) : 10798 세로읽기
#https://www.acmicpc.net/problem/10798

a = []

for _ in range(5):
  a.append(list(input()))

lens = []
for i in range(5):
  lens.append(len(a[i]))

pr = ''
for i in range(max(lens)):
  for j in range(5):
    #list out of range 예외처리
    try:
      pr += a[j][i]
    except:
      continue
 

print(pr)