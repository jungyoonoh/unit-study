# 9079번 동전 게임 (BruteForce) 
# https://www.acmicpc.net/problem/9079

T = int(input())
command = ['111000000', '000111000', '000000111', '100100100', '010010010', '001001001', '100010001', '001010100']

isSelected = [False] * 8

def checkShape(board):
    flag = board[0][0]
    for i in range(3):
        for j in range(3):
            if flag != board[i][j]:
                return False

    return True

def reverseBoard(board, idx):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if command[idx][cnt] == '1':
                board[i][j] *= -1
            cnt += 1
                

def findCase(board, cnt):
    global flag, m
    if checkShape(board):
        flag = True
        m = min(m, cnt)
        
    for i in range(8):
        if not isSelected[i]:
            isSelected[i] = True
            reverseBoard(board, i)
            findCase(board, cnt + 1)
            reverseBoard(board, i)
            isSelected[i] = False
                
    return

# H == 1 / T == -1
for i in range(T):
    board = [[] for _ in range(3)]
    flag = False
    m = 8
    for j in range(3):
        coin = list(map(lambda x: 1 if x == 'H' else -1, input().split()))
        board[j].extend(coin)
    
    findCase(board, 0)
    print(m if flag else -1)