# 1826번 연료 채우기 (Greedy) 
# https://www.acmicpc.net/problem/1826

import heapq

N = int(input()) # 주유소 개수
info = []
totalFuel = 0
for i in range(N):
    a, b = map(int, input().split())
    info.append((a, b)) # 위치, 연료 양
    totalFuel += b
    
L, P = map(int, input().split())
passList = [] # 건너뛴 주유소
info.sort() 
info.append((L, 0)) # 마을 정보
flag = True

remainFuel = P
pos = 0
cnt = 0
for spot, amountOfFuel in info:
    if spot - pos > remainFuel: # 이상태론 못가니 이전 것들을 들렸다고 가정
        while passList and spot - pos > remainFuel:
            remainFuel += (-1) * heapq.heappop(passList)
            cnt += 1        

        if spot - pos > remainFuel:
            flag = False
            break
            
    heapq.heappush(passList, (-1) * amountOfFuel) # 갈 수 있으니 우선 여기 주유소 패스
    remainFuel -= spot - pos
    pos = spot
        
print(cnt if flag else -1)