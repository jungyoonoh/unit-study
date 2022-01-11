#20220110
#백준(구현) : 2615 오목
#https://www.acmicpc.net/problem/2615

# 승부가 결정되지 않았을 경우 0을 언제 넣어야 할지 모르겠음

arr = []
#입력받기
for i in range(19):    
	arr.append(list(map(int, input().split())))

# print(arr)

list1 = [] #1 있는 곳 위치 모음 
list2 = [] #2 있는 곳 위치 모음

#1과 2가 있는 위치를 각각의 리스트에 담아줌
for i in range(19):
    for j in range(19):
        if arr[i][j]==1:
            list1.append([i,j])
        if arr[i][j]==2:
          list2.append([i,j])

# print(list1)
# print(list2)

count_r1 = 0 #가로 1 연속 
count_r2 = 0 #가로 2 연속

##가로
#가로 1
for i in range(len(list1)-1):
  nx = list1[i][0]
  ny = list1[i][1]
  
  #오른쪽 다음 칸 비교
  if (nx == list1[i+1][0]) and (ny+1 == list1[i+1][1]):
    count_r1 += 1 #1이면 count 증가

    #count가 4인 경우 (5개 연속 1인 경우)
    if count_r1 == 4:
      #6개 이상 연속 1인지 확인
      if i+2 < len(list1):
        if (nx == list1[i+2][0]) and (ny+2 == list1[i+2][1]):
          break #6개 이상 1이면 X

        else: #5개만 연속 1이면 출력
          print("1")
          print(list1[i][0]+1, list1[i][1]+1) 

      # # 이 코드 왜 썼었지..? 
      # elif i+2 == len(list1):
      #   print("1")
      #   print(list1[i][0]+1, list1[i][1]+1) 
  
  else: #아니면 count 개수 초기화
    count_r1 = 0

 
#가로 2
for i in range(len(list2)-1):
  nx = list2[i][0]
  ny = list2[i][1]
  if (nx == list2[i+1][0]) and (ny+1 == list2[i+1][1]):
    # ny += 1
    count_r2 += 1
    if count_r2 == 4:
          # print(i,"cc")
          if i+2 < len(list2):
            if (nx == list2[i+2][0]) and (ny+2 == list2[i+2][1]):
              break
            else:
              print("2")
              print(list2[i-3][0]+1, list2[i-3][1]+1) 
          # elif i+2 == len(list2):
          #   print("2")
          #   print(list2[i-3][0]+1, list2[i-3][1]+1) 
  else:
    count_r2 = 0


##세로
#세로 1

# 두번째 요소 기준으로 정렬하기
list3 = sorted(list1, key=lambda x:x[1])
list4 = sorted(list2, key=lambda x:x[1])
# print(list3)
# print(list4)

for i in range(len(list3)-1):
  count_d1 = 0
  nx = list3[i][0]
  ny = list3[i][1]
  if (nx+1 == list3[i+1][0]) and (ny == list3[i+1][1]):
    # ny += 1
    count_d1 += 1
    if count_d1 == 4:
      if i+2 < len(list3):
        if (nx+2 == list3[i+2][0]) and (ny == list3[i+2][1]):
          break
        else:
          print("1")
          print(list3[i-3][0]+1, list3[i-3][1]+1) 
      # elif i+2 == len(list3):
      #   print("1")
      #   print(list3[i-3][0]+1, list3[i-3][1]+1) 

  else:
    count_d1 = 0

for i in range(len(list4)-1):
  count_d2 = 0
  nx = list4[i][0]
  ny = list4[i][1]
  if (nx+1 == list4[i+1][0]) and (ny == list4[i+1][1]):
    count_d2 += 1
    if count_d2 == 4:
      if i+2 < len(list4):
        if (nx+2 == list4[i+2][0]) and (ny == list4[i+2][1]):
          break
        else:
          print("2")
          print(list4[i-3][0]+1, list4[i-3][1]+1) 
      # elif i+2 == len(list4):
      #   print("2")
      #   print(list4[i-3][0]+1, list4[i-3][1]+1) 
 
  else:
    count_d2 = 0

##대각선 - 오른쪽 대각선 / 왼쪽 대각선
#오른쪽 대각선 1

for i1 in list1:
  count_cr1 = 0
  nx = i1[0] +1
  ny = i1[1] +1
  
  for k in range(4):
    if [nx,ny] in list1: #해당하는 값이 리스트에 있는지 확인
      nx+=1
      ny+=1
      count_cr1 +=1 #있으면 count 증가

    else:
      count_cr1 = 0 #없으면 초기화
      break
  
  #count가 4인 경우 (연속 5개) 확인
  if count_cr1 == 4:
    if ([i1[0]-1,i1[1]-1] in list1) or ([i1[0]+5,i1[1]+5] in list1): #연속 6개인지 확인
      continue
    else:#5개만 연속이면 
      print("1")
      print(i1[0]+1, i1[1]+1)

#오른쪽 대각선 2
for i2 in list2:
  count_cr2 = 0
  nx = i2[0] +1
  ny = i2[1] +1
  
  for k in range(4):
    if [nx,ny] in list2:
      nx+=1
      ny+=1
      count_cr2 +=1

    else:
      count_cr2 = 0
      break
  
  if count_cr2 == 4:
    if ([i2[0]-1,i2[1]-1] in list2) or ([i2[0]+5,i2[1]+5] in list2):
      continue
    else:
      print("2")
      print(i2[0]+1, i2[1]+1)


#왼쪽 대각선 1
for i1 in list1:
  nx = i1[0] -1
  ny = i1[1] +1
  count_cl1 = 0
  for k in range(4):
    if [nx,ny] in list1:
      nx += 1
      ny -= 1
      count_cl1 +=1
    else:
      count_cl1 = 0
      break
  
  if count_cl1 == 4:
    if ([nx+1,ny-1] in list1) or ([nx-5,ny+5] in list1):
      continue
    else:
      print("1")
      print(i1[0]+1, i1[1]+1)

#왼쪽 대각선 2
for i2 in list2:
  nx = i2[0] -1
  ny = i2[1] +1
  count_cl2 = 0
  for k in range(4):
    if [nx,ny] in list2:
      nx += 1
      ny -= 1
      count_cl2 +=1
    else:
      count_cl2 = 0
      break
  
  if count_cl2 == 4:
    if ([nx+1,ny-1] in list2) or ([nx-5,ny+5] in list2):
      continue
    else:
      print("2")
      print(i1[0]+1, i1[1]+1)