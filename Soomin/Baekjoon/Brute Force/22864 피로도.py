
#20220301
#백준(완전탐색) : 22864 피로도
#https://www.acmicpc.net/problem/22864

a,b,c,m = map(int,input().split())

# a - 1시간 피로도
# b - 1 시간 일 처리
# c - 1시간 휴식 피로도 감소
# m - 최대 피로도

p = 0
h = 0
count = 0

if a > m:
  print(0)
  exit(0)
else:
  while h != 24:
    h += 1
    if count + a <= m:
      p += b
      count += a
    else:
      if count - c >= 0:
        count -= c
      else:
        count = 0

print(p)