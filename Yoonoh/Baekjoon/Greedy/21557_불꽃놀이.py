# 21557번 불꽃놀이 (Greedy) 
# https://www.acmicpc.net/problem/21557

N = int(input())
data = list(map(int, input().split()))

while True:
    if N == 3:
        data[0] -= 1
        data[-1] -= 1
        break
    
    if data[0] < data[-1]:
        data[-1] -= 1
    else: 
        data[0] -= 1
    N -= 1

print(max(data[0], data[-1]))