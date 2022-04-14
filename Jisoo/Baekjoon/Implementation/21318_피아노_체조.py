# 21318

N = int(input())
nan_N = input()
Q = int(input())

ak = [[0]*2 for m in range(Q)]
nan_N = list(map(int, nan_N.split()))

for i in range(Q):
    xy = input()
    xy = xy.split()
    ak[i][0] = int(xy[0])
    ak[i][1] = int(xy[1])

for x in range(Q): # 4
    count = 0
    for y in range(ak[x][1] - ak[x][0]): #9-5=4, 0 1 2 3
        if ((nan_N[ak[x][0]+y-1]) > (nan_N[ak[x][0]+y])) : # 4>5, 6>7, 7>8
            count = count + 1
    print(count)