# 15665번 N과 M (11) (BackTracking) 
# https://www.acmicpc.net/problem/15665

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
answerPool = set()
def getSequence(seq, idx, cnt):
    
    if cnt == M:
        if len(seq) == 1:
            if seq[0] not in answerPool:
                print(*seq)
                answerPool.add(seq[0])
        else:
            if ''.join(seq) not in answerPool:            
                print(*seq)
                answerPool.add(''.join(seq))
        return        
        
    for i in range(N):
        seq.append(str(data[i]))
        getSequence(seq, i, cnt + 1)
        seq.pop()
    
getSequence([], 0, 0)