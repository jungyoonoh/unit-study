# 4179번 불! (Graph) 
# https://www.acmicpc.net/problem/4179

from collections import deque

R, C = map(int, input().split())
board = []
isVisited = [[False for _ in range(C)] for _ in range(R)]
dy = [-1, 0, 1, 0] # 12 3 6 9
dx = [0, 1, 0, -1]
dq = deque()
for i in range(R):
    data = list(input())
    board.append(data)

    if 'J' in data:
        idx = data.index('J')
        dq.appendleft((i, idx, 'J', 0))
        isVisited[i][idx] = True

    if 'F' in data:
        result = list(filter(lambda x: data[x] == 'F', range(len(data))))
        for res in result:            
            dq.append((i, res, 'F', 0))
            board[i][res] = '#'
            
def escapeMaze():
    flag = False
    while dq:
        y, x, exp, time = dq.popleft()
        
        if exp == 'J':
            if board[y][x] == '#': # 불에 먹힘
                continue
            
            if y == 0 or x == 0 or y == R-1 or x == C-1:
                print(time + 1)
                flag = True
                return flag
        
        for i in range(4):
            ny = y + dy[i]        
            nx = x + dx[i]        
            
            if ny < 0 or nx < 0 or ny >= R or nx >= C:
                continue
            
            if board[ny][nx] == 'F' or board[ny][nx] == '#':
                continue
            
            if exp == 'J' and isVisited[ny][nx]:
                continue
                        
            if board[ny][nx] == '.':
                dq.append((ny, nx, exp, time+1))
                if exp == 'J':
                    isVisited[ny][nx] = True
                else:
                    board[ny][nx] = '#'
                
    return flag

if not escapeMaze():
    print("IMPOSSIBLE")