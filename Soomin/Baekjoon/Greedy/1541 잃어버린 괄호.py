#20220118
#백준(그리디) : 1541 잃어버린 괄호 
#https://www.acmicpc.net/problem/1541

# + 먼저 계산하고 - 계산했을 때가 최소
n = list(input().split('-'))

plus = []

for i in n:
  p = i.split('+')
  hap = 0
  for j in p:
    hap += int(j)
  # + 값들 계산한 리스트  
  plus.append(hap)

ans = plus[0] 

for h in range(1,len(plus)):
  ans -= plus[h]

print(ans)
