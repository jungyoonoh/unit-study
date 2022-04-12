# 12755번 수면 장애 (String) 
# https://www.acmicpc.net/problem/12755

N = int(input())

num = 1
idx = 1
while True:
    N -= idx
    
    if N <= 0:
        p = str(num)
        print(p[len(p) - 1 + N])
        break
    
    num += 1
    if 10 ** idx == num:
        idx += 1