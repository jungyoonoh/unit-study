# 백준 1181 단어 정렬

import sys
input = sys.stdin.readline


lst = set()
for i in range(int(input())):
    word = input().rstrip()
    lst.add((len(word), word))

ans = sorted(lst, key=lambda x: (x[0], x[1]))

for i in ans:
    print(i[1])