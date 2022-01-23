#20220122
#백준(그리디) : 16435 스네이크버드
#https://www.acmicpc.net/problem/16435

n, l = map(int,input().split())

h = list(map(int,input().split()))
h.sort()
i = 0

while True:
  if i < n:
    if l >= h[i]:
      i += 1
      l += 1
    else:
      print(l)
      exit(0)
  else:
    print(l)
    exit(0)
