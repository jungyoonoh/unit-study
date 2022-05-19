# 11725번 트리의 부모 찾기 (Graph) 
# https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(10**9 + 1)
N = int(input())

tree = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)
    
def search(now, tree, parent):
    for next in tree[now]:
        if parent[next] == 0:
            parent[next] = now
            search(next, tree, parent)    

search(1, tree, parent)
for i in range(2, N+1):
    print(parent[i])