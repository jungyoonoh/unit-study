s = list(input())

num = []

alpha = []

for x in range(97,123):
  if chr(x) in s:
    num.append(s.count(chr(x)))
  else:

    num.append(0)




print(*num)