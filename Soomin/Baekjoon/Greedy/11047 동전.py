#20220103
#백준(그리디) : 11047 동전
#https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())

x = []
# 동전 종류를 n만큼 입력 받아 리스트에 넣어줌
for num in range(n):
  x.append(int(input()))

# 최소가 되기 위해서 내림차순 정렬
x.reverse()

coin = 0

for i in x:
  c = k//i # 해당 금액일 때 사용한 동전 수
  price = k - c*i # 남은 금액
  coin += c # 전체 사용 동전 수

  # 0원이 되기 전까지 반복
  if price >= 0:
    k = price 


print(coin)