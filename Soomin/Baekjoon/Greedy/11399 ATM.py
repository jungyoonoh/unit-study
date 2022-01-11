#20220105
#백준(그리디) : 11399 ATM
#https://www.acmicpc.net/problem/11399

n = int(input())
m = list(map(int, input().split()))

#시간 짧은 순으로 배치할 때 전체 소요 시간도 가장 짧음
m.sort()

tl = []
time1 = 0

for j in range(n):
  time1 += + m[j] #각 사람 당 소요 시간
  tl.append(time1) 
  
print(sum(tl)) #전체 소요 시간 = 각 사람 소요 시간 합
