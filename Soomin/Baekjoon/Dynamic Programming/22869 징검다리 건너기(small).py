#20220206
#백준(DP) : 22869
#https://www.acmicpc.net/problem/22869

n,k = map(int,input().split())
a = list(map(int,input().split()))

dp = [-1] * n
dp[0] = 0 #시작점

for i in range(n-1):
  for j in range(i+1, n):
    him = (j-i) * (1 + abs(a[i]-a[j]))
    if dp[i] == -1 and him <= k:
      dp[j] = 0

if dp[-1] == 0:
  print("YES")
else:
  print("NO")

# him = 0
# for i in range(n):
#   if dp[i] == 0:
#     for j in range(i+1,n):
#       if dp[j] == -1:
#         him = (j-i) * (1 + abs(a[i]-a[j]))

#         if k >= him:
#           dp[j] = 0
#       if dp[n-1] == 0:
#         break
#   if dp[n-1] == 0:
#     break

# if dp[n-1] == 0:
#   print('YES')
# else:
#   print('NO')

# print(dp)