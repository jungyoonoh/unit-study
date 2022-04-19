import sys
sys.setrecursionlimit(10000) #

#n, m = map(int, input().split())
n, m = map(int, sys.stdin.readline().split())
# 정점의 개수 n과 간선의 개수 m을 입력

graph = [[] for _ in range(n+1)] # 정점의 개수가 세로인 배열 선언
visited = [False for _ in range(n+1)] # 방문했는지 체크, False로 초기화
graph[0] = [0, 0]

count = 0

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split()) # 간선의 양 끝점 입력
    graph[start].append(end) # start-end 연결
    graph[end].append(start) # end-start 연결
    graph[start].sort() # 정렬
    graph[end].sort() # 정렬

def DFS(start):
    visited[start] = True # 방문했다고 체크

    for i in graph[start]: # 한 줄에서
        if not visited[i]: # False면 DFS 돌려
            DFS(i)

for i in range(1, len(visited)): # 1-6
    if visited[i] == False: # 겹쳐서 안하려고
        count = count + 1 # 갯수
        DFS(i)

# 1 > 2 > 5
# 3 > 4 > 6

print(count)


