#20220405
#백준(구현) : 21318 피아노 체조
#https://www.acmicpc.net/problem/21318


import sys
input = sys.stdin.readline

n = int(input())
lv = list(map(int,input().split()))
dp = [0] * n

#실수 
for i in range(n-1):
  if lv[i] > lv[i+1]:
    dp[i+1] = dp[i] + 1
  else:
    dp[i+1] = dp[i]

# print(dp)

for _ in range(int(input())):
  s, e = map(int,input().split())
  print(dp[e-1]-dp[s-1])

