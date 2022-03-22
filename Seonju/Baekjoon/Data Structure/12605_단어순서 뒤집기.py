# 백준 12605 단어순서 뒤집기

import sys
input = sys.stdin.readline

for i in range(int(input())):
    word = input().rstrip().split()
    print('Case #' + str(i+1) + ':', ' '.join(map(str, word[::-1])))
