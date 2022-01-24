# 백준 16719 ZOAC

import sys
input = sys.stdin.readline

n = list(input().rstrip()) # STEPBACK

if len(n) == 1:
    print(n[0])
    sys.exit(0)

dic = []
for i in range(len(n)):
    dic.append((n[i], i))
dic = sorted(dic) # ABCEKPST

ans = [0 for _ in range(len(n))]
ans[dic[0][1]] = dic[0][0]

while dic:
    print(''.join([k for k in ans if k]))
    i = 1
    idx = 0
    isStart = 1

    while i < len(dic):
        tmp = ans.copy()
        tmp[dic[i][1]] = dic[i][0]

        if isStart:
            dummy = tmp
            isStart = 0
        elif ''.join([k for k in tmp if k]) < ''.join([k for k in dummy if k]):
            dummy = tmp
            idx = i

        i += 1

    ans = dummy
    del dic[idx]