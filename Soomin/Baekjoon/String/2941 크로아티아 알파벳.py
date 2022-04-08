#20220404
#백준(문자열) : 2941 크로아티아 알파벳
#https://www.acmicpc.net/problem/2941

s = input()

c = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in c:
  if i in s:
    s = s.replace(i,'*')

print(len(s))