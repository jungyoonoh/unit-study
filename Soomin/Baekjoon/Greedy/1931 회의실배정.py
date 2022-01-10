#20220104
#백준(그리디) : 1931 회의실배정
#https://www.acmicpc.net/problem/1931

n = int(input())
list1 = []
for i in range(n):
  #시작 ~ 끝 시간 튜플로 받아옴 / 리스트여도 됨
  list1.append(tuple(map(int,input().split())))

#끝나는 시간만 정렬하면 틀림 / 시작시간 기준 우선 정렬 후 끝나는 시간 기준 정렬
list1.sort()
#실제 비교는 끝나는 시간 기준
list1.sort(key=lambda x:x[1])

room = 1 #사용할 수 있는 회의실 최대 개수
end = list1[0][1] #list1에서 끝나는 시간이 가장 빠른 것

#다음 타임부터 비교
for i in range(1, n): 
  #다음 회의 시작 시간 >= 이전 타임 끝나는 시간
  if list1[i][0] >= end:
    room +=1
    end = list1[i][1] #해당 회의 끝나는 시간으로 end 바꿈

# print(list1)

print(room)
