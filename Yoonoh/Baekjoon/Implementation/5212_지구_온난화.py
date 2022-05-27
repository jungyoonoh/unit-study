# 5212번 지구 온난화 (Implementation) 
# https://www.acmicpc.net/problem/5212

R, C = map(int, input().split()) # 가 세

board = []

for i in range(R):
    data = list(input().strip())
    board.append(data)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def getNewBoard(board):
    newBoard = [[] for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                newBoard[i].append('.')
                continue
            cnt = 0
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                
                if ny < 0 or nx < 0 or ny >= R or nx >= C or board[ny][nx] == '.':
                    cnt += 1
                    continue
                
            if cnt >= 3:
                newBoard[i].append('.')
            else:
                newBoard[i].append('X')
                

    return newBoard

def minimize(board):
    startY, startX, endY, endX = 0, 0, 0, 0

    for i in range(R):
        if 'X' in board[i]:
            startY = i
            break
    
    for i in range(R-1, -1, -1):
        if 'X' in board[i]:
            endY = i
            break
    
    flag = False
    for j in range(C):
        for i in range(R):
            if board[i][j] == 'X':
                startX = j
                flag = True
                break      
        if flag:
            break     
    
    flag = False
    for j in range(C-1, -1, -1):
        for i in range(R):
            if board[i][j] == 'X':
                endX = j
                flag = True
                break      
        if flag:
            break               
        
    minimize = []
    for i in range(startY, endY + 1):
        temp = []
        for j in range(startX, endX + 1):
            temp.append(board[i][j])
        minimize.append(temp)
            
    return minimize


newBoard = getNewBoard(board)
minimizeBoard = minimize(newBoard)

for i in range(len(minimizeBoard)):
    print(''.join(minimizeBoard[i]))