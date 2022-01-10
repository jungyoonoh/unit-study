#20220108
#백준(그리디) : 12845 모두의 마블
#https://www.acmicpc.net/problem/12845

#틀렸음 - 반례 모르겠음
n = int(input())
c = list(map(int,input().split()))
level = 0
coin = 0

#카드가 한장 이상인 경우
if len(c) != 1:

  while len(c) != 1:
    maxhap = 0 #최대 합

    #최대 합 찾기
    for i in range(len(c)-1):
      #최대 합 이면
      if c[i]+c[i+1] > maxhap:
        maxhap = c[i]+c[i+1]
        #최대 합을 만드는 카드 중 더 작은 카드 찾기
        if c[i] < c[i+1]:
          level = i
        else:
          level = i+1

    #전체 합
    coin += maxhap

    del c[level] #최대 합 카드 중 작은 카드 삭제


#카드가 한장인 경우 그 한장 레벨 = 골드
else:
  coin = c[0]

print(coin)


  
  
