# 16198번 에너지 모으기 (BruteForce) 
# https://www.acmicpc.net/problem/16198

N = int(input())
data = list(map(int, input().split()))
maxVal = -1
isSelected = [False] * N
def getMaxEnergy(energyList, n, totalEnergy):
    global maxVal
    if n == 2:
        maxVal = max(maxVal, totalEnergy)
        return
    
    now = 0
    for i in range(1, n - 1):
        now = energyList[i]
        totalEnergy += energyList[i-1] * energyList[i+1]
        del energyList[i]
        getMaxEnergy(energyList, n - 1, totalEnergy)
        energyList.insert(i, now)
        totalEnergy -= energyList[i-1] * energyList[i+1]
    
    return

getMaxEnergy(data, N, 0)
print(maxVal)