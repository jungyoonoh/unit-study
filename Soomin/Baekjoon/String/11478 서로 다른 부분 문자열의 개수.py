#20220405
#백준(문자열) : 11478 서로 다른 부분 문자열의 개수
#https://www.acmicpc.net/problem/11478

s = input()
count = set()
for i in range(len(s)):
  for j in range(i,len(s)):
    ss = s[i:j+1]
    count.add(ss)

print(len(count))