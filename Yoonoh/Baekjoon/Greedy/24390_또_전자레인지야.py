# 24390번 또 전자레인지야? (Greedy) 
# https://www.acmicpc.net/problem/24390

H, M = map(int, input().split(':'))
total = int(H) * 60 + int(M)
if total == 0:
    print(0)
    exit(0)
flag = False
cnt = 1
while total > 0:
    if total >= 600:
        total -= 600        
    elif total >= 60:
        total -= 60
    elif total >= 30:
        total -= 30
        flag = True
    else:
        total -= 10
    cnt += 1
if flag:
    cnt -= 1
print(cnt)