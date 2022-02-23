#20220221
#백준(문자열) : 11365 !밀비 급일
#https://www.acmicpc.net/problem/11365

s = ''
while s != 'END':

  s = input()
  if s != 'END':
    print(s[::-1])
  else:
    exit(0)
