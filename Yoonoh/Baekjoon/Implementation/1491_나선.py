# 1491번 나선 (Implementation) 
# https://www.acmicpc.net/problem/1491

# 동 남 서 북 순으로

N, M = map(int, input().split()) # 가로 세로
isVisited = [[False for _ in range(N)] for _ in range(M)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

y = x = dir = 0
isVisited[y][x] = True

def canNotMove(y, x, isVisited):
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= M or nx >= N:
            continue
        
        if not isVisited[ny][nx]:
            return False

    return True

while True:
    while True:
        ny = y + dy[dir]
        nx = x + dx[dir]
        
        if ny < 0 or nx < 0 or ny >= M or nx >= N or isVisited[ny][nx]:
            dir = (dir + 1) % 4
            break
        
        isVisited[ny][nx] = True
        y = ny
        x = nx
    
    if canNotMove(y, x, isVisited):
        print(x, y)
        break