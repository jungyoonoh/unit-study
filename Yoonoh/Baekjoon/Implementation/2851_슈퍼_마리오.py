# 2851번 슈퍼 마리오 (Implementation) 
# https://www.acmicpc.net/problem/2851

score = 0
record = -1
data = []
for _ in range(10):
    data.append(int(input()))
    
for i in range(10):
    score += data[i]
    if abs(record - 100) >= abs(score - 100):
        record = score

print(record)