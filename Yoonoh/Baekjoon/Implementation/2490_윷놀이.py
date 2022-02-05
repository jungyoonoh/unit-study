# 2490번 윷놀이 (Implementation) 
# https://www.acmicpc.net/problem/2490

for i in range(3):
    data = list(map(int, input().split()))
    if data.count(0) == 0:
        print('E')
    elif data.count(0) == 1:
        print('A')
    elif data.count(0) == 2:
        print('B')
    elif data.count(0) == 3:
        print('C')
    elif data.count(0) == 4:
        print('D')