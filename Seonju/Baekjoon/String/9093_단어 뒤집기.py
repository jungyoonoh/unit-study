# 백준 9093 단어 뒤집기

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    stc = input().rstrip().split()
    for i in range(len(stc)):
        print(''.join(stc[i][::-1]), end=' ')
    print()