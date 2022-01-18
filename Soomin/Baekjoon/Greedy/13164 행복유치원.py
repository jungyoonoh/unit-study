#20220116
#백준(그리디) : 13164 행복유치원
#https://www.acmicpc.net/problem/13164

n, k = map(int,input().split())
h = list(map(int,input().split()))

h.sort()
hmin = []

#인접한 원생 키 차이 구함
for i in range(n-1):
  hmin.append(h[i+1] - h[i])

hmin.sort() #차이 적은 순으로 나열
#n-k만큼 차이가 최소
hh = hmin[:n-k]

print(sum(hh))
