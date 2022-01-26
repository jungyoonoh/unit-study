# 21314번 민겸 수 (Greedy) 
# https://www.acmicpc.net/problem/21314

S = list(input())
maxVal = minVal = ""
mCnt = 0 
for i in range(len(S)):
    if S[i] == 'M':
        mCnt += 1
    else:
        if mCnt == 0:
            maxVal += "5"
            minVal += "5"
        else:
            maxVal += "5" + ("0" * mCnt)
            minVal += "1" + ("0" * (mCnt - 1)) + "5"
        mCnt = 0

if mCnt != 0:
    maxVal += "1" * mCnt
    minVal += "1" + "0" * (mCnt - 1)
    
print(maxVal)
print(minVal)