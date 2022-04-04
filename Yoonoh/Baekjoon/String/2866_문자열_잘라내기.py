# 2866번 문자열 잘라내기 (String) 
# https://www.acmicpc.net/problem/2866

R, C = map(int, input().split())
data = []
for _ in range(R):
    data.append(list(input()))
    
converted = []
for i in range(C):
    temp = []
    for j in range(R):
        temp.append(data[j][i])
    converted.append(temp)

count = 0
left, right = 1, R-1
while left <= right:
    pool = set()
    mid = (left + right) // 2
    for i in range(C):        
        pool.add(''.join(converted[i][mid:]))
    
    if len(pool) == C:
        if count < mid:
            count = mid
        left = mid + 1
    else:
        right = mid - 1
    
print(count)