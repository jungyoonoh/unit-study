# 1700번 멀티탭 스케줄링 (Greedy) 
# https://www.acmicpc.net/problem/1700

import heapq
N, K = map(int, input().split())
data = list(map(int, input().split()))
use = set() 
unplug = 0
if N >= K:
    print(0)
else:
    pluged = 0 # 현재 코드 꽂은 개수
    for i in range(K):
        if data[i] in use:
            continue
        
        if pluged < N:
            use.add(data[i])
            pluged += 1
        else:       
            # 앞으로 가장 적게 사용 될 녀석을 찾아서 교환하기
            flag = False            
            for j in list(use):
                if j in data[i:]:
                    continue
                else:
                    use.remove(j)
                    use.add(data[i])
                    unplug += 1
                    flag = True
                    break
            
            if flag: # 뒤에서 사용될 기미가 전혀 없는 녀석이라면.
                continue
                
            # 다 뒤에서 사용될 여지가 있다면, index가 가장 큰 녀석을 뺄것
            candidate = []
            for j in list(use):
                idx = data[i:].index(j) # 최대 힙을 찾아야하므로 인덱스 역수로 넣기
                heapq.heappush(candidate, (-idx, j))
            
            maxTerm = heapq.heappop(candidate)
            use.remove(maxTerm[1])
            use.add(data[i])
            unplug += 1            
            continue

    print(unplug)