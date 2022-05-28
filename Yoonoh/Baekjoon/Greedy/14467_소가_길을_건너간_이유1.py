# 14467번 소가 길을 건너간 이유 1 (Greedy) 
# https://www.acmicpc.net/problem/14467

N = int(input())
cow = [-1 for _ in range(11)]
cnt = 0
for i in range(N):
    num, place = map(int, input().split())
    
    if cow[num] == -1:
        cow[num] = place
        continue
    
    if cow[num] != place:
        cow[num] = place
        cnt += 1
        
print(cnt)