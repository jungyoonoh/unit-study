# 2407번 조합 (Implementation) 
# https://www.acmicpc.net/problem/2407

import math # factorial 모듈을 제공하므로 이를 토대로 nCr 계산 가능 
n, m = map(int, input().split())

def comb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)
print(comb(n, m))