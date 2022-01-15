# 2502번 떡 먹는 호랑이 (DP) 
# https://www.acmicpc.net/problem/2502

d, k = map(int, input().split())

day = [0 for _ in range(d+1)]
day[1] = day[2] = 1

while True:
    for i in range(3, d+1):
        day[i] = day[i-1] + day[i-2]
        
    if day[d] == k:
        print(day[1])
        print(day[2])
        break
    
    if day[-1] > k:
        day[1] += 1
        day[2] = day[1]
        continue
    
    day[2] += 1