# 2422번 한윤정이 이탈리아에 가서 아이스크림을 사먹는데 (BruteForce) 
# https://www.acmicpc.net/problem/2422

N, M = map(int, input().split())

banList = [set() for _ in range(N + 1)] # 조합의 개수만큼

for i in range(M):
    a, b = map(int, input().split())
    banList[a].add(b)
    banList[b].add(a)

cnt = 0

def findCombination(comb, idx, select):
    global cnt
    if select == 3:
        cnt += 1
        return
    
    for i in range(idx, N + 1):
        flag = False
        for j in comb:
            if j in banList[i]:
                flag = True
                break
            
        if flag:
            continue
        
        if i not in comb:
            comb.append(i)
            findCombination(comb, i + 1, select + 1)
            comb.pop()

findCombination([], 1, 0)
print(cnt)