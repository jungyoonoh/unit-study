#20220402
#백준(DP) : 15724 주지수
#https://www.acmicpc.net/problem/15724


import sys
input = sys.stdin.readline
n, m = map(int,input().split())

box = []

for _ in range(n):
  box.append(list(map(int,input().split())))

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, m+1):
    dp[i][j] = box[i-1][j-1] + dp[i][j-1]

# print(dp) 

k = int(input())

for _ in range(k):
  a, b, c, d = map(int,input().split())
  ans = 0
  for i in range(a,c+1):
    ans += dp[i][d] - dp[i][b-1]
  print(ans)
  

# 누적합 시간초과
# from itertools import accumulate
# from itertools import chain
# import sys
# input = sys.stdin.readline
# n, m = map(int,input().split())

# box = []

# for _ in range(n):
#   box.append(list(map(int,input().split())))

# k = int(input())

# kbox = []
# for _ in range(k):
#   kbox.append(list(map(int,input().split())))


# for r in range(k):
#   k = kbox[r]
#   a, b, c, d = k[0]-1, k[1]-1, k[2], k[3]
#   # print(a,b,c,d)
#   # ans = 0
#   kkm =[]
#   for i in range(c):
#     kk = box[i][b:d]
#     kkm.append(kk)
#     # kkm = list(accumulate(box[i][b:d]))
#     # print(kkm)
#     # ans += kkm[-1]
  
#   ans =list(accumulate(chain(*kkm)))
#   print(ans[-1])