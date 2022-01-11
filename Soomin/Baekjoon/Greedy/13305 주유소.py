#20220106
#백준(그리디) : 11305 주유소 
#https://www.acmicpc.net/problem/13305

#1번 방법
n = int(input())
d = list(map(int,input().split()))
o = list(map(int,input().split()))

temp = 0
cost = 0

j = 1

for i in range(n-1):
  if o[i] != 0:
    if o[temp] < o[temp+j]:
      # print("작:",cost)
      # temp = i
      cost += o[temp] * (d[temp] + d[temp+1])
      o[temp+j] = 0
      j+=1
    else:
      # print("큰",cost)
      cost += o[i] * d[i]
      o[i] = 0
      temp += 1
  
print(cost)

#2번 방법 
#(계속 17점 나와서 계속 다시 풀었는데 서브태스트 1번만 고려하면 17점)
n = int(input())
d = list(map(int,input().split()))
o = list(map(int,input().split()))

cost = 0
min_c = d[0] #최소 기름 값

for i in range(n-1):
  #가장 싼 가격이면
  if o[i] < min_c:
    min_c = o[i]
  # 싼 가격으로 이동 * 방금 움직인 거리만큼
  cost += min_c * d[i]

print(cost)
