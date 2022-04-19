# 15654번 N과 M (5) (Graph) 
# https://www.acmicpc.net/problem/15654

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def getSequence(seq, cnt, isSelected):
    
    if cnt == M:
        print(*seq)
        return        
        
    for i in range(N):
        if not isSelected[i]:
            isSelected[i] = True
            seq.append(data[i])
            getSequence(seq, cnt + 1, isSelected)
            seq.pop()
            isSelected[i] = False
    
getSequence([], 0, [False for _ in range(N)])