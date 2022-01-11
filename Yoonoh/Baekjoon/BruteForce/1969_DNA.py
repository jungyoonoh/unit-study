# 1969번 DNA (BruteForce) 
# https://www.acmicpc.net/problem/1969

from collections import defaultdict

N, M = map(int, input().split())
dnaList = [input().strip() for _ in range(N)]

ans = []
sumOfHD = 0
for idx in range(M):
    cnt = defaultdict(int)
    
    for s in dnaList:
        cnt[s[idx]] += 1
        
    keys = sorted(list(cnt.keys()))
    maxVal = 0
    dna = ""
    for i in keys:
        if maxVal < cnt[i]:
            maxVal = cnt[i]
            dna = i
    
    ans.append(dna)
    sumOfHD += sum(cnt.values()) - cnt[dna]

print(''.join(ans))
print(sumOfHD)