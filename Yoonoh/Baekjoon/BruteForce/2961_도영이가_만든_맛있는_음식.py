# 2961번 도영이가 만든 맛있는 음식 (BruteForce) 
# https://www.acmicpc.net/problem/2961

N = int(input())
info = []
isSelected = [False] * N
for i in range(N):
    sourness, bitter = map(int, input().split())
    info.append((sourness, bitter))

def cook(ingredient):
    s, b = 1, 0
    for i in ingredient:
        s *= info[i][0]
        b += info[i][1]
    return abs(s-b)
    
m = 100_000_000_000
def select(ingredient, cnt, idx):
    global m
    if cnt > N:
        return
    
    if cnt > 0:
        m = min(m, cook(ingredient))

    for i in range(idx, N):
        if not isSelected[i]:
            isSelected[i] = True
            ingredient.append(i)
            select(ingredient, cnt + 1, i + 1)
            ingredient.pop()
            isSelected[i] = False

select([], 0, 0)
print(m)