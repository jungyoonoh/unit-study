# 1389번 케빈 베이컨의 6단계 법칙 (Graph) 
# https://www.acmicpc.net/problem/1389

from collections import deque

N, M = map(int, input().split())
info = [[] for _ in range(N+1)]
matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    info[A].append(B)
    info[B].append(A)

def bfs(s):
    
    dq = deque()
    dq.append((s, s, 0)) # start, now, length
    isVisited = [False] * (N+1)
    isVisited[s] = True
    
    while dq:
        start, now, length = dq.popleft()
        if matrix[start][now] < length:
            matrix[start][now] = length
        
        for next in info[now]:
            if not isVisited[next]:
                isVisited[next] = True
                dq.append((start, next, length + 1))
    

for i in range(1, N+1):
    bfs(i)

idx = 1
minVal = sum(matrix[1])
for i in range(2, N+1):
    comp = sum(matrix[i])
    if minVal > comp:
        idx = i
        minVal = comp

print(idx)