# 10808번 알파벳 개수 (Implementation) 
# https://www.acmicpc.net/problem/10808

S = list(input())
alphabet = [0] * 26
for i in S:
    alphabet[ord(i) - ord('a')] += 1
print(*alphabet)