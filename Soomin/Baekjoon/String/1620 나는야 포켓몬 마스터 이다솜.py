#20220401
#백준(문자열) : 1620 나는야 포켓몬 마스터 이다솜
#https://www.acmicpc.net/problem/1620

n, m = map(int,input().split())

pocket = []
for _ in range(n):
  pocket.append(input())

q = []
for _ in range(m):
  q.append(input())

for i in q:
  if i.isdigit():
    print(pocket[int(i)-1])
  else:
    print(pocket.index(i)+1)