# 14469번 소가 길을 건너간 이유 3 (Greedy) 
# https://www.acmicpc.net/problem/14469

N = int(input())

data = []
for i in range(N):
    arrive, time = map(int, input().split())
    data.append((arrive, time))

data.sort(key = lambda x:(x[0], -x[1]))

total = 0
for arrive, time in data:
    if total < arrive:
        total = arrive    
    total += time
    
print(total)