# 12833번 XORXORXOR (Bitmasking) 
# https://www.acmicpc.net/problem/12833

A, B, C = map(int, input().split())
print(A ^ B if C % 2 == 1 else A)