# 8983번 사냥꾼 (BinarySearch) 
# https://www.acmicpc.net/problem/8983

import bisect

M, N, L = map(int, input().split()) # 사대 수, 동물 수, 사거리
gunSpot = list(map(int, input().split()))
gunSpot.sort()
animalSpot = [] 
for i in range(N):
    x, y = map(int, input().split())
    animalSpot.append((x, y))

animalSpot.sort()
move = [-1, 0, 1]
animalNumInRange = 0
for x, y in animalSpot:
    idx = bisect.bisect_left(gunSpot, x)
    
    for i in move:
        case = idx + i
        if case < 0 or case >= M:
            continue
        
        if y + abs(gunSpot[case] - x) <= L:
            animalNumInRange += 1
            break

print(animalNumInRange)