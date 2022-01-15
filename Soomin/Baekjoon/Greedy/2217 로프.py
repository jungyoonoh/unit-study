#20220115
#백준(그리디) : 2217 로프
#https://www.acmicpc.net/problem/2217

n = int(input())
k = []
for i in range(n):
  k.append(int(input()))

k.sort(reverse=True)

nk = []

#가장 큰 값부터 w/k 나눴을 때 가장 큰 값 찾기
for i in range(n):
  nk.append(k[i]*(i+1))

print(max(nk))
