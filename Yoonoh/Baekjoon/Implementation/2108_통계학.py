# 2108번 통계학 (Implementation) 
# https://www.acmicpc.net/problem/2108

from collections import defaultdict

N = int(input())
dd = defaultdict(int)
data = []
for i in range(N):
    num = int(input())
    data.append(num)
    dd[num] += 1

freq = []
freqVal = max(dd.values())
for key in dd.keys():
    if dd[key] == freqVal:
        freq.append(key)
        
freq.sort()        
data.sort()
print(round(sum(data) / N))
print(data[N//2])
print(freq[0] if len(freq) <= 1 else freq[1])
print(max(data) - min(data))