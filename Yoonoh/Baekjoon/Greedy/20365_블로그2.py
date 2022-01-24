# 20365번 블로그2 (Greedy) 
# https://www.acmicpc.net/problem/20365

N = int(input())
data = list(input())
standard = data[0]
color = idx = 1
while idx < N:
    if standard != data[idx]:
        color += 1
        i = idx + 1
        while i < N and data[idx] == data[i]:
            i += 1
        idx = i
    else:
        idx += 1
    
print(color)