#20220218
#백준(문자열) : 9342 염색체
#https://www.acmicpc.net/problem/9342

import sys, re
input = sys.stdin.readline

n = int(input())
al = re.compile('^[A-F]{0,1}A+F+C+[A-F]{0,1}$') #문자열 검증
# ^ : 문자열 처음
# $ : 마지막
# [A-F] : A-F까지
# {0,1} : 반복 횟수, 0~1번 반복
# https://wikidocs.net/4308



for _ in range(n):
  s = input().strip()

  ok = al.match(s)
  if (ok != None):
    print("Infected!")
  else:
    print("Good")
