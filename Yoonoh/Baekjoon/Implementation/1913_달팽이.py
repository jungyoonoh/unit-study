# 1913번 달팽이 (Implementation) 
# https://www.acmicpc.net/problem/1913

N = int(input())
find = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

board[N // 2][N // 2] = 1
y = x = N // 2

dy = [-1, 0, 1, 0] # 12 3 6 9
dx = [0, 1, 0, -1]

repeatNum = 1
fillNum = 2
dir = 0
flag = True
ans = []
while flag:
    for i in range(repeatNum):
        ny = y + dy[dir]
        nx = x + dx[dir]
        board[ny][nx] = fillNum
        
        if fillNum == find:
            ans.extend([ny + 1, nx + 1])
        
        fillNum += 1
        
        y = ny
        x = nx
        if y == 0 and x == 0:
            flag = False
            break
    
    dir = (dir + 1) % 4
    if dir % 4 == 0 or dir % 4 == 2:
        repeatNum += 1

if len(ans) == 0:
    ans.extend([N // 2 + 1, N // 2 + 1])

for i in range(len(board)):
    print(*board[i])
print(*ans)