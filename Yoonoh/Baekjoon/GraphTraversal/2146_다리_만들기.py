# 2146번 다리 만들기 (BFS) 
# https://www.acmicpc.net/problem/2146

# BFS로 최단 경로를 찾을 껀데, 서로 다른 그룹을 반드시 찾아야만 함. 같은 곳은 X 

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
world = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def markUpMap():
    isVisited = [[False for _ in range(N)] for _ in range(N)]    
    markUpedMap = [[0 for _ in range(N)] for _ in range(N)]
    
    marker = 1
    for i in range(N):
        for j in range(N):
            if world[i][j] != 0 and not isVisited[i][j]:
                marking(markUpedMap, marker, i, j, isVisited)            
                marker += 1
            
    return markUpedMap

def marking(markUpedMap, marker, i, j, isVisited):
    
    isVisited[i][j] = True
    markUpedMap[i][j] = marker
    
    dq = deque()
    dq.append((i, j))
    
    while dq:
        y, x = dq.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            
            if isVisited[ny][nx] or world[ny][nx] != world[y][x]: 
                continue
            
            isVisited[ny][nx] = True
            markUpedMap[ny][nx] = marker
            dq.append((ny, nx))
            
    return


def findCandidate(markUpedMap):
    
    candidateSpot = []
    for i in range(N):
        for j in range(N):
            if markUpedMap[i][j] != 0:
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    
                    if ny < 0 or nx < 0 or ny >= N or nx >= N:
                        continue
                    
                    if markUpedMap[ny][nx] == 0:
                        candidateSpot.append((i, j))
                        break
                    
    return candidateSpot

def bfs(markUpedMap, i, j):
    
    dq = deque()
    isVisited = [[False for _ in range(N)] for _ in range(N)]
    dq.append((i, j, 0))
    isVisited[i][j] = True
    
    color = markUpedMap[i][j]
    minVal = 10001
    while dq:
        y, x, time = dq.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            
            if isVisited[ny][nx]:
                continue
            
            if markUpedMap[ny][nx] != 0 and markUpedMap[ny][nx] != color:
                minVal = min(minVal, time)
                continue
            
            isVisited[ny][nx] = True
            dq.append((ny, nx, time + 1))
    
    return minVal

markUpedMap = markUpMap()
candidateSpot = findCandidate(markUpedMap)
ans = 10001
for i, j in candidateSpot:
    ans = min(ans, bfs(markUpedMap, i, j))
    
print(ans)