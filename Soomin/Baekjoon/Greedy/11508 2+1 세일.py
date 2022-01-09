#20220109
#백준(그리디) : 11508 2+1 세일
#https://www.acmicpc.net/problem/11508

n = int(input())
c = []

for i in range(n):
  c.append(int(input()))

#가장 비싼 순으로 3개씩 자를 때 최소 합
c.sort(reverse=True) 

th = n // 3 #3개씩 묶음이 몇 개 나오는지
cc = c[0:3*th] #2+1 되는 것들만 따로 담음
cost = 0 #최소 가격 합

for i in range(len(cc)):
  #제일 싼 가격 빼고 가격 더함
  if i%3 != 2: 
    cost += cc[i]

#2개씩 가격 + 3개 묶음 되지 않은 것들 가격
print(cost+sum(c[3*th:]))