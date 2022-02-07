#20220207
#백준(이분탐색) : 7795 먹을 것인가 먹힐 것인가
#https://www.acmicpc.net/problem/7795

import sys
import bisect
#bisect : 이분탐색

input = sys.stdin.readline
num = int(input())

while num:
  bi = 0

  n, m = map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))

  a.sort()
  b.sort()

  for i in a:
    bi += bisect.bisect_left(b,i) #왼쪽 인덱스 구하기

  print(bi)
  num -= 1