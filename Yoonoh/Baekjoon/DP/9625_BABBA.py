# 9625번 BABBA (DP) 
# https://www.acmicpc.net/problem/9625

K = int(input())
A = [0] * 46
B = [0] * 46
B[2] = A[2] = B[1] = 1

for i in range(3, 46):
    A[i] = A[i-1] + A[i-2]
    B[i] = B[i-1] + B[i-2]

print(A[K], B[K])