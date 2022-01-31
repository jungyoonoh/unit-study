#20220125
#백준(그리디) : 1439 뒤집기 
#https://www.acmicpc.net/problem/1439


n = list(str(input()))

temp = n[0] #현재 위치 문자
count = 0

for i in n:
  #현재 문자랑 다르면서 n[0]이랑도 다르면 count 증가
  if i != temp and i != n[0]:
    count += 1
    temp = i

  else:
    temp = i

print(count)