#20220205
#백준(완전탐색) : 2304 창고 다각형
#https://www.acmicpc.net/problem/2304

n = int(input()) #기둥 개수

lh = []

for _ in range(n):
  lh.append(list(map(int, input().split())))

lh.sort()

start = lh[0][1]
max1 = sorted(lh,reverse = True)
max1 = sorted(max1,reverse=True, key=lambda x:x[1])

maxi = lh.index(max1[0])
w = lh[0][0]
hap = 0

for i in range(maxi):
  if lh[i][1] >= lh[i+1][1]:
    lh[i+1][1] = lh[i][1]

for i in range(n-1, maxi, -1):
  if lh[i][1] >= lh[i-1][1]:
    lh[i-1][1] = lh[i][1]

for i in range(maxi):
  hap += (lh[i+1][0] - lh[i][0]) * lh[i][1]

for i in range(n-1, maxi, -1):
  hap+= (lh[i][0] - lh[i-1][0]) * lh[i][1]

hap += max1[0][1]
print(hap)
