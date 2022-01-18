#20220116
#백준(구현) : 15787 기차가 어둠을 헤치고 은하수를
#https://www.acmicpc.net/problem/15787

N,M = map(int,input().split())
m = [] #조건
for i in range(M):
  m.append(list(map(int,input().split())))

# train = [[0]*20] * N 하면 안됨!
train = []
for _ in range(N):
  train.append([0]*20)

#조건 개수만큼 for문 실행
for i in range(M):
  #조건 1
  if m[i][0] == 1:
    seat = train[m[i][1]-1][m[i][2]-1]
    # 해당 기차, 해당 자리가 비어있으면 -> 사람 태움
    if seat == 0:
      seat = 1
  
  #조건 2
  elif m[i][0] == 2:
    seat = train[m[i][1]-1][m[i][2]-1]
    #해당 기차, 해당 자리가 차있으면 -> 사람 하차
    if seat == 1:
      seat = 0

  #조건 3
  elif m[i][0] == 3:
    ind =[] #사람이 앉아있는 곳 인덱스 체크
    for j in range(20):
      if train[m[i][1]-1][j] == 1:
        ind.append(j)

    # 20번 좌석에 사람이 있으면
    if 19 in ind:
      train[m[i][1]-1][19] = 0 #하차 시킴
      # 한 칸씩 +1
      for d in range(len(ind)-1): 
        train[m[i][1]-1][ind[d]] = 0
      for d in range(len(ind)-1):
        train[m[i][1]-1][ind[d]+1] = 1     
    else:
      # 한 칸씩 +1
      for d in ind:
        train[m[i][1]-1][d] = 0
      for d in ind:
        train[m[i][1]-1][d+1] = 1 
      
  #조건 4    
  elif m[i][0] == 4:
    ind1 = [] #사람이 앉아있는 곳 인덱스 체크
    for j in range(20):
      if train[m[i][1]-1][j] == 1:
        ind1.append(j)
    
    # 1번 좌석에 사람이 있으면
    if 0 in ind1:
      train[m[i][1]-1][0] = 0 #하차 시킴
      # 한 칸씩 -1
      for d in range(1,len(ind1)):
        train[m[i][1]-1][ind1[d]] = 0
      for d in range(1,len(ind1)): 
        train[m[i][1]-1][ind1[d]-1] = 1
    else:
      # 한 칸씩 -1
      for d in ind1:
        train[m[i][1]-1][d] = 0
      for d in ind1:
        train[m[i][1]-1][d-1] = 1      

# 최종 기차에서 중복 체크
train = list(map(tuple,train))
count = len(set(train))
print(count)

