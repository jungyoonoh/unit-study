#20220116
#백준(구현) : 14719 빗물
#https://www.acmicpc.net/problem/14719

h, w = map(int,input().split())

block = list(map(int,input().split()))

# w*h 이차원 리스트
b = [[0 for _ in range(w)] for _ in range(h)]

k = 0
# 블록이 있는 공간은 1 넣어줌
for i in block:
  for j in range(i):
    b[j][k] = 1
  k += 1
# print(b)
"""
[[1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 1, 1, 1, 0, 0, 1], 
[1, 0, 0, 1, 1, 0, 0, 0], 
[0, 0, 0, 0, 1, 0, 0, 0]]
"""
hap = 0 #채워지는 빗물 양

for i in range(h):
  # 블록이 아예 없거나 / 이미 블록으로 다 차있는 곳은 빗물이 고일 수 없음
  if 0 in b[i] and 1 in b[i]:
    water = 0
    ind = b[i].index(1) #블록 시작 위치

    for j in range(ind,w): 
      if b[i][j] == 1:
        hap += water #빗물 전체 합
        water = 0
      else: #블록이 없는 경우 빗물 채움
        water += 1

print(hap)