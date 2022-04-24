# 15655번 N과 M (6) (Graph) 
# https://www.acmicpc.net/problem/15655

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def getSequence(seq, idx, cnt, isSelected):
    
    if cnt == M:
        print(*seq)
        return        
        
    for i in range(idx, N):
        if not isSelected[i]:
            isSelected[i] = True
            seq.append(data[i])
            getSequence(seq, i, cnt + 1, isSelected)
            seq.pop()
            isSelected[i] = False
    
getSequence([], 0, 0, [False for _ in range(N)])