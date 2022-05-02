# 2357번 최솟값과 최댓값 (Segment Tree) 
# https://www.acmicpc.net/problem/2357

import sys
from math import *
input = sys.stdin.readline

N, M = map(int, input().split())
data = []
h = int(ceil(log2(N)))
treeMin = [0] * (1 << (h+1))
treeMax = [0] * (1 << (h+1))

for _ in range(N):
    data.append(int(input()))
    
def initMin(index, start, end):
    if start == end:
        treeMin[index] = data[start]
        return treeMin[index]
    
    mid = (start + end) // 2
    treeMin[index] = min(initMin(index * 2, start, mid), initMin(index * 2 + 1, mid + 1, end))
    return treeMin[index]

def initMax(index, start, end):
    if start == end:
        treeMax[index] = data[start]
        return treeMax[index]
    
    mid = (start + end) // 2
    treeMax[index] = max(initMax(index * 2, start, mid), initMax(index * 2 + 1, mid + 1, end))
    return treeMax[index]

def searchMin(index, start, end, left, right):
    if start > right or end < left:
        return 1e10 + 1
    
    if left <= start and end <= right:
        return treeMin[index]
    
    mid = (start + end) // 2
    return min(searchMin(index * 2, start, mid, left, right), searchMin(index * 2 + 1 , mid + 1, end, left, right))

def searchMax(index, start, end, left, right):
    if (start > right or end < left):
        return 0
    
    if left <= start and end <= right:
        return treeMax[index]
    
    mid = (start + end) // 2
    return max(searchMax(index * 2, start, mid, left, right), searchMax(index * 2 + 1, mid + 1, end, left, right))

initMin(1, 0, N-1)
initMax(1, 0, N-1)
for _ in range(M):
    s, e = map(int, input().split())
    print(searchMin(1, 0, N - 1, s - 1, e - 1), searchMax(1, 0, N - 1, s - 1, e - 1))