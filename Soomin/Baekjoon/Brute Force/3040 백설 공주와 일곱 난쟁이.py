#20220302
#백준(완전탐색) : 3040 백설 공주와 일곱 난쟁이
#https://www.acmicpc.net/problem/3040

from itertools import combinations


num = []
for _ in range(9):
  num.append(int(input()))

nan = list(combinations(num,7))

# print(nan)

for i in nan:
  if sum(i) == 100:
    for j in i:
      print(j)