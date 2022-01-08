# 백준 2594 놀이공원

import sys
input = sys.stdin.readline

ride = [[600, 600], [1320, 1320]]
for _ in range(int(input())):
    x, y = input().split()
    x = int(x[:2]) * 60 + int(x[2:]) - 10
    y = int(y[:2]) * 60 + int(y[2:]) + 10
    ride.append([x, y])
ride.sort()

rest = 0
last = 600

for run, stop in ride:
    rest = max(rest, run - last)
    last = max(last, stop)

print(rest)