# 5568번 카드 놓기 (BruteForce) 
# https://www.acmicpc.net/problem/5568

n = int(input())
k = int(input())

cardList = []
for i in range(n):
    cardList.append(int(input().strip()))
    
ans = set()
isSelected = [False] * n

def makeBundle(pick, idx, cnt):
    if cnt == k:
        num = ''.join(pick)
        if num not in ans:
            ans.add(num)
        return
        
    for i in range(n):
        if not isSelected[i]:
            isSelected[i] = True
            pick.append(str(cardList[i]))
            makeBundle(pick, i + 1, cnt + 1)
            pick.pop()
            isSelected[i] = False
            
    return

makeBundle([], 0, 0)
print(len(list(ans)))