#20220106
#백준(구현) : 1913 달팽이
#https://www.acmicpc.net/problem/1913

n = int(input()) 
loc = int(input())

# n*n 2차원 배열에 0 넣어줌
a = [[0] * n for i in range(n)]

# 이동할 네 가지 방향 벡터 정의(상 하 좌 우)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
nx,ny = 0, 0 #최초 위치

#n*n ~ 1 순으로 담은 배열
n2 = []
for i in range(n*n,0,-1):
  n2.append(i)
print(n2)


change = 0 #변화 
j = 0 #n2 증가용

#n*n+(2*n-2) : change가 총 2*n-2번 일어나기 때문
for k in range(n*n+(2*n-2)):

  #찾는 값 위치
  if (n2[j] == loc):
    loc_x = nx
    loc_y = ny

  #범위 벗어나거나 이미 채워진 곳일 때
  if (nx < 0) or (ny < 0) or (nx >= n) or (ny >= n) or (a[nx][ny] != 0):
    #현재 위치에서 바로 직전 위치로 이동
    nx -= dx[change%4]
    ny -= dy[change%4]

    #방향 전환
    change +=1

    #방향 전환 후 위치
    nx += dx[change%4]
    ny += dy[change%4]

  #채울 수 있는 곳일 때
  else:
    a[nx][ny] = n2[j] 
    nx += dx[change%4]
    ny += dy[change%4]
    j+=1 #실제 값 채워질 때만 n2 인덱스 번호 증가

#문제 주워진 형태로 출력    
for p in range(n):
  for q in range(n):
    print(a[p][q], end=' ')
  print("\n")

print(loc_x, loc_y)     


