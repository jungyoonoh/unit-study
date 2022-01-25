# 14620번 꽃길 (BruteForce) 
# https://www.acmicpc.net/problem/14620

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
isSelected = [[False for _ in range(N)] for _ in range(N)]

dy = [0, -1, 0, 1, 0] # 본인, 12 3 6 9
dx = [0, 0, 1, 0, -1]

def calcCost(spot):
    flower = set()
    for s in spot:
        for i in range(5):
            ny = s[0] + dy[i]
            nx = s[1] + dx[i]
            if ny >= 0 and nx >= 0 and ny < N and nx < N and (ny, nx) not in flower:
                flower.add((ny, nx))
            else:
                return 200 * 16
        
    res = 0
    for i in list(flower):
        res += board[i[0]][i[1]]
        
    return res

cost = 200 * 16 # M
def findSpot(spot, cnt):
    global cost
    
    if cnt == 3:
        cost = min(cost, calcCost(spot))
        return
    
    for i in range(N):
        for j in range(N):
            if not isSelected[i][j]:
                isSelected[i][j] = True
                spot.append((i, j))
                findSpot(spot, cnt + 1)
                spot.pop()
                isSelected[i][j] = False

findSpot([], 0)
print(cost)