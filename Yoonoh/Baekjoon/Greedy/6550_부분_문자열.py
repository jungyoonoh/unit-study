# 6550번 부분 문자열 (Greedy) 
# https://www.acmicpc.net/problem/6550

import sys
input = sys.stdin.readline

while True:
    sentence = input().strip()
    if not sentence:
        break
    s, t = sentence.split()
    idx = 0
    lenS = len(s)
    flag = False
    for i in range(len(t)):
        if s[idx] == t[i]:
            idx += 1
        if idx == lenS:
            flag = True
            break
    print("Yes" if flag else "No")