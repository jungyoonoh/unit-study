# 20366번 같이 눈사람 만들래? (TwoPointer) 
# https://www.acmicpc.net/problem/20366

N = int(input())
snow = list(map(int, input().split()))
snow.sort()
minVal = 2 * (10 ** 9 - 1)

for elsaStart in range(N-3): # 597
    for elsaEnd in range(elsaStart+3, N): # 597
        elsaSnow = snow[elsaStart] + snow[elsaEnd]
        annaStart, annaEnd = elsaStart + 1, elsaEnd - 1
        
        while annaStart < annaEnd: # avg 298
            annaSnow = snow[annaStart] + snow[annaEnd]
            if minVal > abs(elsaSnow - annaSnow):
                minVal = abs(elsaSnow - annaSnow)
        
            if minVal == 0:
                print(0)
                exit(0)
            
            if elsaSnow < annaSnow:
                annaEnd -= 1
            else:
                annaStart += 1

print(minVal)