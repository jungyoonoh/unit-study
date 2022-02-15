# 3687번 성냥개비 (DP) 
# https://www.acmicpc.net/problem/3687

TC = int(input())

# 성냥 n개로 만들 수 있는 값
minDp = [888888888888888] * 101 # 성냥 100개 이상 소모되는 값
minDp[2] = 1
minDp[3] = 7
minDp[4] = 4
minDp[5] = 2
minDp[6] = 6
minDp[7] = 8
minDp[8] = 10
add = [1,7,4,2,0,8]

maxDp = [0] * 101
maxDp[2] = 1
maxDp[3] = 7

# maxVal
for i in range(4, 101):
    maxDp[i] = int(str(maxDp[i-2]) + '1')
    
# minVal
for i in range(9, 101):
    for j in range(2, 8): # 0 ~ 5 
        minDp[i] = min(minDp[i], int(str(minDp[i-j]) + str(add[j-2])))

for i in range(TC):
    matches = int(input())
    print(minDp[matches], maxDp[matches])