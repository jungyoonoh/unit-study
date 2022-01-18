# 백준 20207 달력

import sys
input = sys.stdin.readline

# 일정 입력받으면서 달력에 채우기
cal = [0 for _ in range(365)]
for i in range(int(input())):
    start, end = map(int, input().split())
    for j in range(start, end + 1):
        cal[j-1] += 1

# 코팅지 넓이 구하기
ans, width, height = 0, 0, 0
for i in cal:
    if i:
        width += 1
        height = max(height, i)
    else:
        ans += width * height
        width, height = 0, 0
ans += width * height

print(ans)
