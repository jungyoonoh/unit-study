# 17609번 회문 (String) 
# https://www.acmicpc.net/problem/17609

TC = int(input())

for _ in range(TC):
    S = input().strip()
    SL = len(S)
    stack = 0
    for i in range(SL // 2):
        if S[i] != S[SL - i - 1]:
            sub = S[i:SL - i]
            subL = len(sub)
            for j in range(subL // 2):
                if sub[j+1] != sub[subL - j - 1]:
                    stack += 1
                    break
            
            for j in range(subL // 2):
                if sub[j] != sub[subL - j - 2]:
                    stack += 1
                    break
            
            stack = 1 if stack <= 1 else 2
            
        if stack:
            break
   
    print(stack)