#20220223
#백준(문자열) : 20291 파일 정리
#https://www.acmicpc.net/problem/20291

n = int(input())
name = []
count = {}
for _ in range(n):
  s, a = input().split('.')
  name.append(a)

for i in name:
  try:
    count[i] += 1
  except:
    count[i] = 1

nn = list(count.items())
nn.sort()

for j in nn:
  print(j[0],j[1])