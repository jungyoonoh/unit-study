# 1254번 팰린드롬 만들기 (BruteForce) 
# https://www.acmicpc.net/problem/1254

word = input().strip()
for i in range(len(word)):
    if word[i:] == word[i:][::-1]:
        print(len(word) + i)
        break