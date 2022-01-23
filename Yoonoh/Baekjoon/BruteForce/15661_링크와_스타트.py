# 15661번 링크와 스타트 (BruteForce) 
# https://www.acmicpc.net/problem/15661

N = int(input())
stat = [list(map(int, input().split())) for _ in range(N)]
m = 9999999
isSelected = [False] * N
total = set(i for i in range(N))
def calcStatGap(L):
    link = list(L)
    start = list(total - L) 
    linkStat = startStat = 0
    
    for i in link:
        for j in link:
            if i != j:
                linkStat += stat[i][j]

    for i in start:
        for j in start:
            if i != j:
                startStat += stat[i][j]                                

    return abs(linkStat - startStat)   

def matching(member, cnt, idx):
    global m
    if cnt < N:
        m = min(m, calcStatGap(member))
    else:
        return
    
    for i in range(idx, N):
        if not isSelected[i]:
            isSelected[i] = True
            member.add(i)
            matching(member, cnt + 1, i)
            member.remove(i)
            isSelected[i] = False
            
matching(set(), 0, 0)
print(m)