#20220320
#백준(문자열) : 20154 이 구역의 승자는 누구야?!
#https://www.acmicpc.net/problem/20154

a = [0 for _ in range(65)]

b = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

a += b

# print(a)
s = list(map(ord,input()))
  
# print(s)
hap = 0
for i in s:
  hap += a[i]

if (hap % 10) % 2:
  print("I'm a winner!")
else:
  print("You're the winner?")