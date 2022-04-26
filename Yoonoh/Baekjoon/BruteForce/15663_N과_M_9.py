# 15663번 N과 M (9) (BackTracking) 
# https://www.acmicpc.net/problem/15663

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
answerPool = set()
def getSequence(seq, idx, cnt, isSelected):
    
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
        if not isSelected[i]:
            isSelected[i] = True
            seq.append(str(data[i]))
            getSequence(seq, i, cnt + 1, isSelected)
            seq.pop()
            isSelected[i] = False
    
getSequence([], 0, 0, [False for _ in range(N)])