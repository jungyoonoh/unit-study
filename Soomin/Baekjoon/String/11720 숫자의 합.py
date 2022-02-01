#20220129
#백준(문자열) : 11720 숫자의 합
#https://www.acmicpc.net/problem/11720

n = int(input())

s = list(map(int,input()))

hap = 0
for i in s:
  hap += i
print(hap)