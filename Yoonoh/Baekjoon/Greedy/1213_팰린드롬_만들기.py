# 1213번 팰린드롬 만들기 (Greedy) 
# https://www.acmicpc.net/problem/1213

from collections import defaultdict

S = input().strip()

alphabet = defaultdict(int)

for i in range(len(S)):
    alphabet[S[i]] += 1

cnt = 0
flag = True
last = "None"
for i in alphabet.keys():
    if alphabet[i] % 2 == 1:
        last = i
        cnt += 1
        if cnt > 1:
            flag = False
            break
        
candidate = sorted(alphabet.keys())
ans = []
L = len(candidate)
i = 0
if flag:
    while i < L:
        if alphabet[candidate[i]] > 1:
            alphabet[candidate[i]] -= 2
            ans.append(candidate[i])
        else:
            i += 1

    tail = ans[::-1]
    if last != "None":
        ans.append(last)
    ans.extend(tail)
    print(''.join(ans))
else:
    print("""I'm Sorry Hansoo""")