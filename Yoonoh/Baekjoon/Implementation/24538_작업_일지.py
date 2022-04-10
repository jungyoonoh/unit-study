# 24538번 작업 일지 (Implementation) 
# https://www.acmicpc.net/problem/24538

import sys
import itertools
input = sys.stdin.readline

N, K = map(int, input().split())
work = [0] * (K+2) # 1일 ~ K일
lastCostOfWorker = [0] * (K+2)
for _ in range(N):
    start, end = map(int, input().split())
    work[start] += 1
    work[end + 1] -= 1
    lastCostOfWorker[end + 1] += (end - start + 1) # 일 그만두면 이사람 만큼 빠짐

data = list(itertools.accumulate(work))

ans = [0] * (K+2)
cost = 0 # 하루에 벌어들이는 돈의 양
workingNow = 0
for i in range(1, K+1):
    if i == 1 and data[i] > 0:
        cost = workingNow = data[i]        
        ans[i] = cost
        continue

    cost -= lastCostOfWorker[i]            
    workingNow = data[i] # 현재 일하고 있는 사람들
    cost += workingNow    
    ans[i] = cost

print(*ans[1:K+1])