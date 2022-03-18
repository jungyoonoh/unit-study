# 10825번 국영수 (Implementation) 
# https://www.acmicpc.net/problem/10825

N = int(input())
data = []
for i in range(N):
    name, kor, eng, math = list(map(str, input().split()))
    data.append((int(kor), int(eng), int(math), name))
    
data.sort(key=lambda x:(-x[0], x[1], -x[2], x[3]))

for i in range(N):
    print(data[i][3])