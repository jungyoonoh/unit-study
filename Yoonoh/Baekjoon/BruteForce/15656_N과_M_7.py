# 15656번 N과 M (7) (Graph) 
# https://www.acmicpc.net/problem/15656

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def getSequence(seq, cnt):
    
    if cnt == M:
        print(*seq)
        return        
        
    for i in range(N):
        seq.append(data[i])
        getSequence(seq, cnt + 1)
        seq.pop()
    
getSequence([], 0)