# 1769번 3의 배수 (String) 
# https://www.acmicpc.net/problem/1769

N = input()
ans = 0
flag = False
def findNum(num, cnt):
    global ans, flag
    if int(num) < 10:
        ans = cnt
        flag = True if int(num) % 3 == 0 else False
        return

    nextNum = 0
    for i in range(len(num)):
        nextNum += int(num[i])
    
    findNum(str(nextNum), cnt + 1)
    return

findNum(N, 0)
print(ans)
print("YES" if flag else "NO")