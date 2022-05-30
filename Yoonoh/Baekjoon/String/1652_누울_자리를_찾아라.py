# 1652번 누울 자리를 찾아라 (String) 
# https://www.acmicpc.net/problem/1652

N = int(input())

check = ['.', '.', 'X']
board = []
temp = ['X' for _ in range(N+2)]
board.append(temp)
for i in range(N):
    data = list(input())
    data.insert(0, 'X')
    data.append('X')
    board.append(data)
board.append(temp)

w, h = 0, 0
N += 2
for i in range(N):
    for j in range(N-2):
        flag = True
        for k in range(3):
            if check[k] != board[i][j+k]:
                flag = False
                break
        
        if flag:
            w += 1
            
for i in range(N):
    for j in range(N-2):
        flag = True
        for k in range(3):
            if check[k] != board[j+k][i]:
                flag = False
                break
        
        if flag:
            h += 1

print(w, h)