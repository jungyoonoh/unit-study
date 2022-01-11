# 2615번 오목 (BruteForce) 
# https://www.acmicpc.net/problem/2615

# 19 x 19
board = [list(map(int, input().split())) for _ in range(19)]

# 가로 세로 우하향 우상향을 나타내는 방향벡터 선언
dy = [0, 1, 1, -1]
dx = [1, 0, 1, 1]

def determineWinner(y, x):       
    standard = board[y][x]    
    for i in range(4):
        ny, nx = y, x
        flag = True
        
        for _ in range(4):
            ny += dy[i]
            nx += dx[i]
            
            if ny < 0 or ny >= 19 or nx < 0 or nx >= 19 or standard != board[ny][nx]:                
                flag = False
                break
                        
        if flag:
            if y - dy[i] >= 0 and y - dy[i] < 19 and x - dx[i] >= 0 and x - dx[i] < 19 and standard == board[y - dy[i]][x - dx[i]]:
                continue
            if ny + dy[i] >= 0 and ny + dy[i] < 19 and nx + dx[i] >= 0 and nx + dx[i] < 19 and standard == board[ny + dy[i]][nx + dx[i]]:
                continue
            
            print(standard)
            print(y + 1, x + 1)
            return True
        
    return False

isDetermined = False
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            if determineWinner(i, j):
                isDetermined = True
                break
            
    if isDetermined:
        break

if not isDetermined:
    print(0)