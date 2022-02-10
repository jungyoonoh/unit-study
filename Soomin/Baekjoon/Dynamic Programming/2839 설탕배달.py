#20220210
#백준(DP) : 2839 설탕 배달
#https://www.acmicpc.net/problem/2839

n = int(input())

a = [5001] * (n+5)

a[3] = a[5] = 1

for i in range(6, n+1):
  a[i] = min(a[i-3],a[i-5]) +1

if a[n] < 5001:
  print(a[n])
else:
  print(-1)

  