# 2170번 선 긋기 (Implementation) 
# https://www.acmicpc.net/problem/2170

N = int(input())
data = []
for i in range(N):
    start, end = map(int, input().split())
    data.append((start, end))

data.sort()
s, e = data[0][0], data[0][1]
res = 0
for i in range(1, N):
    ns, ne = data[i]
    
    if e < ns:
        res += e-s
        s, e = ns, ne    
    elif ne > e:
        e = ne

res += e-s
print(res)