#20220114
#백준(그리디) : 20365 블로그2
#https://www.acmicpc.net/problem/20365

n = int(input())
c = list(input())
c.append('E')
count = [1] * 2

#파란색으로 다 칠한 경우
for i in range(n):
  if c[i] == 'B':
    continue
  elif c[i] == 'R':
    count[0] += 1
    if c[i+1] == 'R':
      count[0] -= 1
      continue

#빨간색으로 다 칠한 겨우
for j in range(n):
  if c[j] == 'R':
    continue
  elif c[j] == 'B':
    count[1] += 1
    if c[j+1] == 'B':
      count[1] -= 1
      continue


print(min(count))