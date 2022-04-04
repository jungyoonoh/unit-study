# 1644번 소수의 연속합 (TwoPointer) 
# https://www.acmicpc.net/problem/1644

N = int(input())

for i in range(1, 3):
    if N == i:
        print(i-1)
        exit(0)

prime = [1] * (N+1)
primePool = []
for i in range(2, N+1):
    if prime[i] == 0:
        continue
    
    for j in range(i * 2, N+1, i):
        prime[j] = 0

for i in range(2, N+1):
    if prime[i] == 1:
        primePool.append(i)

start, end, cnt = 0, 1, 0
L = len(primePool)
sumOfPrime = primePool[start] + primePool[end]
while end <= L:
    if primePool[end] > N:
        break
        
    if sumOfPrime == N:
        cnt += 1
        
    if sumOfPrime <= N:
        end += 1
        if end == L:
            break
        sumOfPrime += primePool[end]
    else:
        sumOfPrime -= primePool[start]
        start += 1

print(cnt)