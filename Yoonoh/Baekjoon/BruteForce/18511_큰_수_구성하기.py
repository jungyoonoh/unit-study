# 18511번 큰 수 구성하기 (BruteForce) 
# https://www.acmicpc.net/problem/18511

# 아 K자리를 구하라는게 아니었다..

import itertools

N, K = map(int, input().split())
Z = list(map(str, input().split()))

for i in range(len(str(N)), 0, -1):
    ans = []
    w = list(itertools.product(Z, repeat = i))
    for candidate in w:
        ret = int(''.join(candidate))
        if ret <= N:
            ans.append(ret)
    
    if len(ans) >= 1:
        print(max(ans))
        break