# 백준 11365 !밀비 급일

import sys
input = sys.stdin.readline


while True:
    stc = input().rstrip()
    if stc == 'END':
        break
    print(stc[::-1])