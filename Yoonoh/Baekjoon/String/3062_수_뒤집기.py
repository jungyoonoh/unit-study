# 3062번 수 뒤집기 (String) 
# https://www.acmicpc.net/problem/3062

N = int(input())

def rev(n):
    if n < 10:
        return n
    reverse = []
    while n:
        reverse.append(str(n % 10))
        n = n // 10
    return int(''.join(reverse))

def isSymmetry(num):
    num = str(num)
    L = len(num)
    R = (len(num) // 2) + 1 if len(num) % 2 == 1 else len(num) // 2
    for i in range(R):
        if num[i] != num[L - 1 - i]:
            return False
    return True

for _ in range(N):
    num = int(input())
    revNum = rev(num)
    if isSymmetry(num + revNum):
        print("YES")
    else:
        print("NO")
    