#20220107
#백준(그리디) : 4796 캠핑
#https://www.acmicpc.net/problem/4796

end = 0
list1 = []
end_check = 1
day = []

while end_check != end:
  L, P, V = map(int, input().split())
  end_check = L+P+V
  list1.append([L, P, V])

for i in list1:
  if i[0] == 0 and i[1] == 0 and i[2] == 0:
    break
  if i[2] % i[1] >= i[0]:
    day.append(i[2] // i[1] * i[0] + i[0])
  else:
    day.append(i[2] // i[1] * i[0] + i[2] % i[1])

for j in range(len(day)):
  print("Case %d: %d" % (j+1,day[j]))

# print(list1)


