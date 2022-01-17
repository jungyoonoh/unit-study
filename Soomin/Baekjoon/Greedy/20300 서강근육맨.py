#20220113
#백준(그리디) : 20300 서강근육맨
#https://www.acmicpc.net/problem/20300

n = int(input())

list1 = list(map(int, input().split()))

list1.sort()

m = []
m1 = []


if n % 2 == 0:
  for i in range(n//2):
    #작은 수 + 큰 수 합 리스트에 담기
    m.append(list1[i]+list1[n-1-i])
  print(max(m)) #작은 수 + 큰 수 합 중 최대

else:
  # n이 홀수일 때 마지막 날은 근손실양 제일 큼(단일)
  m1.append(list1[n-1])
  for i in range(n//2):
    m1.append(list1[i]+list1[n-2-i]) #작은 수 + 큰 수 합
  print(max(m1)) #중 최대