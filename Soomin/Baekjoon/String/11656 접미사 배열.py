#20220402
#백준(문자열) : 11656 접미사 배열
#https://www.acmicpc.net/problem/11656

s = list(input())

sn = []

for i in range(len(s)):
  sn.append(''.join(s[i:]))

sn.sort()
for i in sn:
  print(i)