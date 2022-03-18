# 5427번 불 (Graph) 
# https://www.acmicpc.net/problem/5427

from collections import deque
TC = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def escapeBuilding(board, dq, isVisited, w, h):
    
    while dq:
        y, x, time = dq.popleft()
        
        if time > -1 and board[y][x] != '*':
            if y == 0 or y == h - 1 or x == 0 or x == w - 1:
                print(time + 1)
                return True            
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= h or nx >= w:
                continue
            
            if board[ny][nx] == '#' or board[ny][nx] == '*':
                continue
            
            if time > -1:
                if isVisited[ny][nx] or board[ny][nx] != '.':
                    continue
                isVisited[ny][nx] = True
                dq.append((ny, nx, time + 1))
            else:
                board[y][x] = '#'
                board[ny][nx] = '*'
                dq.append((ny, nx, -1))
        
    return False

for i in range(TC):
    w, h = map(int, input().split())
    dq = deque()
    isVisited = [[False for _ in range(w)] for _ in range(h)]
    board = []
    for i in range(h):
        data = list(input())
        board.append(data)
        if '@' in data:
            idx = data.index('@')
            dq.appendleft((i, idx, 0))
            isVisited[i][idx] = True
        
        if '*' in data:
            result = list(filter(lambda x : data[x] == '*', range(len(data))))
            for fire in result:
                dq.append((i, fire, -1))

    if not escapeBuilding(board, dq, isVisited, w, h):
        print("IMPOSSIBLE")