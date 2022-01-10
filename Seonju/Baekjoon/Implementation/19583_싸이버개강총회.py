# 백준 19583 싸이버개강총회

import sys
input = sys.stdin.readline

start, end, stream = input().split()
start = int(start[:2] + start[3:])
end = int(end[:2] + end[3:])
stream = int(stream[:2] + stream[3:])

attend = set()
cnt = 0

while True:
    try:
        time, name = input().split()
        time = int(time[:2] + time[3:])
        if time <= start:
            attend.add(name)
        elif end <= time <= stream and name in attend:
            attend.remove(name)
            cnt += 1
    except:
        break

print(cnt)