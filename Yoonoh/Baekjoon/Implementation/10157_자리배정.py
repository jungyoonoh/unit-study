# 10157번 자리 배정 (Implementation) 
# https://www.acmicpc.net/problem/10157

C, R = map(int, input().split()) # 가로 세로 
K = int(input())

def rotateSquare(standard, cnt):
    
    # 아래
    for i in range(standard, R - standard):
        cnt += 1
        if cnt == K:
            print(standard + 1, i + 1)
            return
    
    # 오른쪽
    for i in range(standard + 1, C - standard):
        cnt += 1
        if cnt == K:
            print(i + 1, R - standard)
            return
    
    # 위
    for i in range(R - standard - 2, standard - 1, -1):
        cnt += 1
        if cnt == K:
            print(C - standard, i + 1)
            return
    
    # 왼쪽
    for i in range(C - standard - 2, standard, -1):
        cnt += 1
        if cnt == K:
            print(i + 1, standard + 1)
            return
    
    return

if C * R < K:
    print(0)
else:
    w, h, remain, standard, cnt = C, R, K, 0, 0
    while True:
        nw, nh = w - 2, h - 2
        if nw < 0: nw = 0
        if nh < 0: nh = 0
        circumference = (w * h) - (nw * nh)
        if remain - circumference <= 0:
            rotateSquare(standard, cnt)
            break
        else:
            standard += 1
            cnt += circumference
            w, h = nw, nh
            remain -= circumference