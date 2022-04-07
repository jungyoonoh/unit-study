# 1515번 수 이어 쓰기 (String) 
# https://www.acmicpc.net/problem/1515

S = input().strip()
L = len(S)
now = 1
idx = 0
flag = False
while True:
    data = list(str(now))
    for i in range(len(data)):
        if S[idx] == data[i]:
            idx += 1
    
        if idx == L:
            flag = True
            break

    if flag:
        print(now)
        break

    now += 1