#20220222
#백준(문자열) : 1181 단어 정렬
#https://www.acmicpc.net/problem/1181

n = int(input())
word = []
for _ in range(n):
  word.append(input())

word = list(set(word))
word.sort()
word.sort(key=len)

for i in word:
  print(i)
  