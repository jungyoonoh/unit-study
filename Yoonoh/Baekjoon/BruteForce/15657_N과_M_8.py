# 15657번 N과 M (8) (Graph) 
# https://www.acmicpc.net/problem/15657

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def getSequence(seq, idx, cnt):
    
    if cnt == M:
        print(*seq)
        return        
        
    for i in range(idx, N):
        seq.append(data[i])
        getSequence(seq, i, cnt + 1)
        seq.pop()
    
getSequence([], 0, 0)