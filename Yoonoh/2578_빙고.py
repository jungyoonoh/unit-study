# 2578번 빙고 (Implementation) 
# https://www.acmicpc.net/problem/2578

def checkBingo():
    bingoNum = 0
    
    # 가로
    for i in range(5):
        cnt = 0
        for j in range(5):
            if not isSelected[i][j]:
                break
            cnt += 1
        if cnt == 5:
            bingoNum += 1

    # 세로
    for i in range(5):
        cnt = 0
        for j in range(5):
            if not isSelected[j][i]:
                break
            cnt += 1
        if cnt == 5:
            bingoNum += 1
            
    # 대각선
    cnt = 0
    for i in range(5):
        if not isSelected[i][i]:        
            break
        cnt += 1
        
    if cnt == 5:
        bingoNum += 1
    
    cnt = 0
    for i in range(5):
        if not isSelected[i][4 - i]:
            break
        cnt += 1
        
    if cnt == 5:
        bingoNum += 1
    
    return bingoNum
    
board = [list(map(int, input().split())) for _ in range(5)]
isSelected = [[False for _ in range(5)] for _ in range(5)]

grid = dict()
for i in range(5):
    for j in range(5):
        grid[board[i][j]] = (i, j)
        
numList = []
for i in range(5):
    numList.extend(list(map(int, input().split())))
    
turn = 0    
for i in numList:    
    turn += 1
    y, x = grid[i]
    isSelected[y][x] = True
    if turn >= 12:
        if checkBingo() >= 3:
            print(turn)
            break