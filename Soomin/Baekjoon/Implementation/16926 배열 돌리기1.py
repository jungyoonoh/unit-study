#20220131
#백준(구현) : 16926 배열 돌리기1
#https://www.acmicpc.net/problem/16926

n, m, r = map(int,input().split())
list1 = []

for _ in range(n):
  list1.append(list(map(int,input().split())))
a = []

lenm = m
lenn = n
start = 0

# → ↓ ← ↑ 순서로 리스트에 담아줌
for k in range(min(n,m)//2):
  b = []
  for j in range(start,lenm):
    b.append(list1[start][j])
  for l in range(start+1,lenn-1):
    b.append(list1[l][lenm-1])
  for o in range(lenm-1,start-1,-1):
    b.append(list1[lenn-1][o])
  for p in range(lenn-2,start,-1):
    b.append(list1[p][start])
  start += 1
  lenm -= 1
  lenn -= 1
  a.append(b)
# [[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5], [6, 7, 11, 10]]

# 회전
for k in range(len(a)):
  for q in range(r):
    que = a[k][0]
    a[k].pop(0)
    a[k].append(que)
#[[3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 1, 2], [11, 10, 6, 7]]

# 돌려진 숫자를 맞춰서 넣어줌
lenm = m
lenn = n
start = 0
for k in range(min(n,m)//2):
  num = len(a[k])
  st = 0
  while st != num:
    for j in range(start,lenm):
      list1[start][j] = a[k][st]
      st +=1
    for l in range(start+1,lenn-1):
      list1[l][lenm-1] = a[k][st]
      st +=1
    for o in range(lenm-1,start-1,-1):
      list1[lenn-1][o] = a[k][st]
      st +=1
    for p in range(lenn-2,start,-1):
      list1[p][start] = a[k][st]
      st +=1
    start += 1
    lenm -= 1
    lenn -= 1
#print(list1)

#출력
for i in list1:
  print(*i, sep = ' ')
  # *쓰면 []없어짐

