# 10868번 최솟값 (Segment Tree) 
# https://www.acmicpc.net/problem/10868

import sys
from math import *
input = sys.stdin.readline

N, M = map(int, input().split())
data = []
h = int(ceil(log2(N)))
tree = [0] * (1 << (h+1))

for _ in range(N):
    data.append(int(input()))
    
def init(index, start, end):
    if start == end:
        tree[index] = data[start]
        return tree[index]
    
    mid = (start + end) // 2
    tree[index] = min(init(index * 2, start, mid), init(index * 2 + 1, mid + 1, end))
    return tree[index]

def search(index, start, end, left, right):
    if start > right or end < left:
        return 1e10 + 1
    
    if left <= start and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    return min(search(index * 2, start, mid, left, right), search(index * 2 + 1 , mid + 1, end, left, right))

init(1, 0, N-1)
for _ in range(M):
    s, e = map(int, input().split())
    print(search(1, 0, N-1, s - 1, e - 1))