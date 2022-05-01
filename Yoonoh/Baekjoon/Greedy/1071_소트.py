# 1071번 소트 (Greedy) 
# https://www.acmicpc.net/problem/1071

N = int(input())
data = list(map(int, input().split()))

data.sort()
pool = set()
cnt = [0] * 1001
for i in range(N):
    pool.add(data[i])
    cnt[data[i]] += 1

maxVal = max(data)
ans = []
i = 0
while True:
    if len(ans) == N:
        break
    
    if data[i] not in pool:
        i += 1
        continue
    
    if data[i] + 1 <= 1000 and (data[i] + 1) in pool:
        idx = data[i] + 2
        flag = True
        while idx not in pool:
            if idx > maxVal:
                flag = False
                break                 
            idx += 1
        
        if idx <= 1000 and flag:
            for j in range(cnt[data[i]]):
                ans.append(data[i])
            ans.append(idx)
            pool.remove(data[i])
            cnt[data[i]] = 0
            cnt[idx] -= 1
            if cnt[idx] == 0:
                pool.remove(idx)
        else:
            ans.append(data[i] + 1)
            cnt[data[i] + 1] -= 1
            if cnt[data[i] + 1] == 0:
                pool.remove(data[i] + 1)
    else:
        for j in range(cnt[data[i]]):
            ans.append(data[i])
        cnt[data[i]] = 0
        pool.remove(data[i])

print(*ans)