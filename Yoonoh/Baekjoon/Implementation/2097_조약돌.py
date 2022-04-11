# 2097번 조약돌 (Implementation) 
# https://www.acmicpc.net/problem/2097

import math
N = int(input())
if N <= 4:
    print(4)
else:
    square = -1
    r = 4
    for i in range(2, math.ceil(math.sqrt(N) + 1)):
        if i ** 2 < N:
            r += 4
            continue
            
        square = i
        break
    
    if (square - 1) ** 2 + square >= N:
        r -= 2
    
    print(r)