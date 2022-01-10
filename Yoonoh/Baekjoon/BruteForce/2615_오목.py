# 2615번 오목 (BruteForce) 
# https://www.acmicpc.net/problem/2615

# 다섯 개의 바둑알 중에서 가장 왼쪽에 있는 바둑알을 출력해야 한다

# 19 x 19
board = [list(map(int, input().split())) for _ in range(19)]
SIZE = 19

def determineWinner(y, x):   
    standard = board[y][x]
    
    # 가로    
    flag = True
    for i in range(1, 5):
        if x + i >= 19 or standard != board[y][x+i]:
            flag = False
            break
    
    if flag:
        if x == 0 and standard != board[y][x+5]:
            return standard
        elif x == 14 and standard != board[y][x-1]:
            return standard
        elif (x != 0 and x != 14) and standard != board[y][x-1] and standard != board[y][x+5]:
            return standard
        
    # 세로
    flag = True
    for i in range(5):
        if y + i >= 19 or standard != board[y+i][x]:
            flag = False
            break

    if flag:
        if y == 0 and standard != board[y+5][x]:
            return standard
        elif y == 14 and standard != board[y-1][x]:
            return standard
        elif (y != 0 and y != 14) and standard != board[y-1][x] and standard != board[y+5][x]:
            return standard
        
    # 우하향
    flag = True
    for i in range(5):
        if x + i >= 19 or y + i >= 19 or standard != board[y+i][x+i]:
            flag = False
            break
    
    if flag:
        if (x == 0 or y == 0) and (x == 14 or y == 14):
            return standard
        elif (x == 0 or y == 0) and standard != board[y+5][x+5]:
            return standard
        elif (x == 14 or y == 14) and standard != board[y-1][x-1]:
            return standard
        elif (x != 0 and y != 0) and (x != 14 and y != 14) and standard != board[y-1][x-1] and standard != board[y+5][x+5]:
            return standard

    # 우상향
    flag = True
    for i in range(5):
        if x + i >= 19 or y - i < 0 or standard != board[y-i][x+i]:
            flag = False
            break

    if flag:
        if (x == 0 or y == 18) and (x == 15 or y == 4):
            return standard
        elif (x == 0 or y == 18) and standard != board[y-5][x+5]:
            return standard
        elif (x == 15 or y == 4) and standard != board[y+1][x-1]:
            return standard
        elif (x != 0 and y != 18) and (x != 15 and y != 4) and standard != board[y+1][x-1] and standard != board[y-5][x+5]:
            return standard
    
    return 0

isDetermined = False
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            ret = determineWinner(i, j)
            if ret != 0:
                print(ret)
                print(i+1, j+1)
                isDetermined = True
                break
            
    if isDetermined:
        break

if not isDetermined:
    print(0)