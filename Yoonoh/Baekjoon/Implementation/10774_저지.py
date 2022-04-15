# 10774번 저지 (Implementation) 
# https://www.acmicpc.net/problem/10774

J = int(input())
A = int(input())
isSelected = [False] * (J+1)
sizeInfo = {'S':0, 'M':1, 'L':2}
info = ['a'] 
for _ in range(J):
    info.append(input().strip())

ans = 0
for _ in range(A):
    size, num = input().split()
    num = int(num)
    if not isSelected[num] and sizeInfo[info[num]] >= sizeInfo[size]:
        isSelected[num] = True
        ans += 1

print(ans)