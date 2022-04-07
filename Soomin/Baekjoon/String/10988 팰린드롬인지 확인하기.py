#20220407
#백준(문자열) : 10988 팰린드롬인지 확인하기
#https://www.acmicpc.net/problem/10988

n = list(input())

a = n[:len(n)//2]
b = n[::-1]
b = b[:len(n)//2]  

if a == b:
  print(1)
else:
  print(0)  