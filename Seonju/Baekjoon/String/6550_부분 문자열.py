# 백준 6550 부분 문자열

import sys
input = sys.stdin.readline

while True:
    tmp = input().rstrip()
    if not tmp:
        break
    s, t = tmp.split()

    s_idx = 0
    for t_content in t:
        if s_idx == len(s):
            break
        if t_content == s[s_idx]:
            s_idx += 1

    if s_idx == len(s):
        print('Yes')
    else:
        print('No')