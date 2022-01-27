# 24389번 2의 보수 (Bitmasking) 
# https://www.acmicpc.net/problem/24389

N = int(input())
T = ~N
T += 1
comp = (1 << 32) - 1
A = N & comp
B = T & comp
res = bin(A ^ B).count('1')
print(res)