# 15666번 N과 M (12) (BackTracking) 
# https://www.acmicpc.net/problem/15666

def getSequence(seq, cnt):
    cnt -= 1
    if cnt == -1:
        print(*seq)
        return
    
    for i in arr:
        if not seq or i >= seq[-1]:
            getSequence(seq+[i],cnt)

n,m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
getSequence([], m)