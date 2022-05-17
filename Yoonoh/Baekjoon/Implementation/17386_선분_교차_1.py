# 17386번 선분 교차 1 (Implementation) 
# https://www.acmicpc.net/problem/17386

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def judgeSpot(y1, x1, y2, x2, targetY, targetX):
    return ((targetY - y1) * (x2 - x1)) - ((y2 - y1) * (targetX - x1))

if judgeSpot(y1, x1, y2, x2, y3, x3) * judgeSpot(y1, x1, y2, x2, y4, x4) < 0 and judgeSpot(y3, x3, y4, x4, y1, x1) * judgeSpot(y3, x3, y4, x4, y2, x2) < 0:
    print(1)
else:
    print(0)