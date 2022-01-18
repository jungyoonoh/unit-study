#20220112
#백준(그래프 탐색) : 2606 바이러스
#https://www.acmicpc.net/problem/2606

n = int(input()) #컴퓨터 수 
c = int(input()) #컴퓨터 쌍 수

def dfs(graph,v,visited):
  visited[v] = True
  
  for i in graph[v]:
    if visited[i] == False:
      #if not visited[i]
      dfs(graph, i, visited)
  return True
  

#그래프 2차원, 인접
graph = [[] for _ in range(n+1)]

for _ in range(c):
  num1, num2 = map(int,input().split())
  graph[num1].append(num2)
  graph[num2].append(num1)

visited = [False] * (n+1)

dfs(graph,1,visited)
print(sum(visited)-1)



