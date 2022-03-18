# 1244번 스위치 켜고 끄기 (Implementation) 
# https://www.acmicpc.net/problem/1244

N = int(input())
switch = [0] + list(map(int, input().split()))
studentNum = int(input())

for _ in range(studentNum):
    sex, switchNum = map(int, input().split())
    if sex == 1:
        multiple = 1
        while switchNum * multiple < N + 1:
            switch[switchNum * multiple] = 0 if switch[switchNum * multiple] == 1 else 1
            multiple += 1
    else:
        dx = 1
        switch[switchNum] = 0 if switch[switchNum] == 1 else 1
        while switchNum - dx > 0 and switchNum + dx < N + 1:
            if switch[switchNum - dx] == switch[switchNum + dx]:
                switch[switchNum - dx] = 0 if switch[switchNum - dx] == 1 else 1
                switch[switchNum + dx] = 0 if switch[switchNum + dx] == 1 else 1
            else:
                break
                    
            dx += 1

for i in range(1, len(switch)):
    print(switch[i], end = ' ')
    if i % 20 == 0:
        print()