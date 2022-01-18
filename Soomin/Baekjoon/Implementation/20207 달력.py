#20220116
#백준(구현) : 20207 달력
#https://www.acmicpc.net/problem/20207

n = int(input())
day = []
for i in range(n):
  day.append(list(map(int,input().split())))

cal = [0]*365 #365개 만들어줌

for i in range(n):
  day1 = day[i][0] #시작 날
  day2 = day[i][1] #끝나는 날
  for j in range(day1,day2+1):
    cal[j-1] +=1 #일자 별로 일정 개수 체크하기

w = 0 #가로
h = 0 #세로
hap = 0 

for k in range(365):
  #일정이 있는 경우
  if cal[k] != 0:
    w += 1 #가로 길이 늘려줌
    if cal[k] > h:
      h = cal[k] #가장 큰 세로 값 찾음
    if k == 364: #365일인 경우는 0을 만나지 못하므로
      hap += w*h #~365일까지 값 더해줌

  #0을 만났을 경우
  else:
    hap += w * h #0 만나기 전까지 가로*세로
    w = 0 #가로, 세로 초기화
    h = 0

#1일 ~ 365일 모두 일정이 있는 경우
if hap == 0:
  hap = w*h

print(hap)

  
# 바보 같은 삽질의 흔적 ^^
# day.sort(key=lambda x:x[1], reverse=True)
# day.sort(key=lambda x:x[0])
# cal = [[]]
# num = 0

# #일정 표시
# for j in range(n):
#   #첫 줄에 표시할 수 있으면
#   if day[j][0] not in cal[0]:
#      for v in range(day[j][1]-day[j][0]+1):
#         cal[0].append(day[j][0]+v)
#   #첫 줄에 이미 일정이 있을 때      
#   else:
#     #일정이 한 줄 밖에 없으면 바로 다음 줄에 새로운 일정 추가
#     if len(cal) == 1:
#       new = []
#       for w in range(day[j][1]-day[j][0]+1):
#         new.append(day[j][0]+w)
#       cal = cal + [new]
  
#     #일정이 2줄 이상
#     else:
#       #2번 째 줄부터 검사
#       for y in range(1,len(cal)):
#         #해당 줄에 일정이 들어갈 수 있으면
#         if day[j][0] not in cal[y]:
#           for v in range(day[j][1]-day[j][0]+1):
#             cal[y].append(day[j][0]+v) 
#             num = 0
#           break
#         #일정이 들어갈 수 없는 경우
#         else:
#           num = 1
#       # num = 1로 끝났다는 것은 일정이 어느 곳에도 들어갈 수 없다. 따라서 새로운 줄 추가
#       if num == 1:
#         new = []
#         for w in range(day[j][1]-day[j][0]+1):
#           new.append(day[j][0]+w)
#         cal = cal + [new]
  
