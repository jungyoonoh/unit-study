#20220304
#백준(그래프 탐색) : 2667 단지번호붙이기
#https://www.acmicpc.net/problem/2667

n = int(input())

z = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
count = 0
ans = []

def dfs(i, j):
  #global 선언
  global count
  count +=1
  visited[i][j] = 1

  
  # 동서남북 확인
  for w in range(4):
    x = i + dx[w]
    y = j + dy[w]
    # 범위 안쪽
    if 0 <= x < n and 0 <= y < n:
      #집이 있는 곳이지만, 아직 방문하지 않았으면 탐색 시작
      if visited[x][y] == 0 and z[x][y] == 1:
        dfs(x, y)

for i in range(n):
  for j in range(n):
    if z[i][j] == 1 and visited[i][j] == 0:
      count = 0
      dfs(i, j)
      ans.append(count)

print(len(ans))

ans.sort()
for i in ans:
  print(i)