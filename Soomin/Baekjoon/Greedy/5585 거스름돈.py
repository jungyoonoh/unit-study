#20220127
#백준(그리디) : 5585 거스름돈
#https://www.acmicpc.net/problem/5585

n = int(input())

money = [500, 100, 50, 10, 5, 1]
joi = 1000 - n
count = 0

for i in money:
  if joi >= i:

    count += joi//i
    joi -= joi//i * i

print(count)
