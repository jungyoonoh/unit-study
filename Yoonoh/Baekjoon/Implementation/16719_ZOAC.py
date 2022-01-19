# 16719번 ZOAC (Implementation) 
# https://www.acmicpc.net/problem/16719

S = list(map(lambda x:ord(x[0]) - ord('A'), list(input())))
L = len(S)
isSelected = [False] * L

def findFlag():
    s = e = -1
    findStart = False
    for i in range(L-1, -1, -1):
        if not findStart and not isSelected[i]:
            s = i
            findStart = True
            continue
        
        if findStart and isSelected[i]:
            e = i
            break
    
    return (s, e)

start, end = L-1, -1
while True:
    m, idx, ans = 26, -1, ""
    for i in range(start, end, -1):
        if not isSelected[i] and S[i] <= m:
            m, idx = S[i], i
        
    if idx == -1:
        start, end = findFlag()
        continue
    
    isSelected[idx] = True
    start, end = findFlag()
    for i in range(L):
        if isSelected[i]:
            ans += chr(S[i] + ord('A'))
            
    print(ans)
    
    if len(ans) == L:
        break