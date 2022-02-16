# 22857번 가장 긴 짝수 연속한 부분 수열 (small) (DP) 
# https://www.acmicpc.net/problem/22857

N, K = map(int, input().split())
seq = list(map(int, input().split()))

maxVal = 0
if N == 1:
    maxVal = 1 if seq[0] % 2 == 0 else 1
    print(maxVal)
    exit(0)

oddCnt = [0] * N
oddCnt[0] = 1 if seq[0] % 2 == 1 else 0
for i in range(1, N):
    oddCnt[i] = oddCnt[i-1] + 1 if seq[i] % 2 == 1 else oddCnt[i-1]

for i in range(1, N):
    left, right = 0, i
    while left <= right:
        mid = (left + right) // 2
        now = 1 if seq[mid] % 2 == 1 else 0 # 현재 위치 정보 갱신
        if oddCnt[i] - oddCnt[mid] + now <= K:
            right = mid - 1
        else:
            left = mid + 1
    
    lBound = right + 1
    now = 1 if seq[lBound] % 2 == 1 else 0 # 현재 위치 정보 갱신
    maxVal = max(maxVal, (i - lBound + 1) - (oddCnt[i] - oddCnt[lBound] + now))

print(maxVal)

# i는 고정된 기준값을 수행하고
# left와 right의 바운드 안에서 K의 범위를 넘지않는 index 값의 최대 범위를 수행할 수 있다. 
# right + 1 ~ i 의 경우는 반드시 홀수의 개수가 K보다 작거나 같음을 만족하므로, 범위의 최댓값을 빠르게 찾는 이분 탐색을 이용한다.