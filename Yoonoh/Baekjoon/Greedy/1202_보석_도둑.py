# 1202번 보석 도둑 (Greedy) 
# https://www.acmicpc.net/problem/1202

import heapq
import sys
input = sys.stdin.readline

jewel = []
bag = []
N, K = map(int, input().split())
for i in range(N):
    M, V = map(int, input().split())
    jewel.append((M, V))

for i in range(K):
    bag.append(int(input()))

jewel.sort()
bag.sort()

canGetList = []
ans = 0
for w in bag:
    while jewel and jewel[0][0] <= w:
        heapq.heappush(canGetList, -jewel[0][1])
        heapq.heappop(jewel) # 무게 기준으로 정렬했기때문에 앞에서부터 쳐내짐
    
    if canGetList:
        ans += heapq.heappop(canGetList) # 현재 가질 수 있는것중에 가장 비싼 보석
    elif not jewel:
        break # 더이상 찾을 수 있는 보석 X

print(-ans)