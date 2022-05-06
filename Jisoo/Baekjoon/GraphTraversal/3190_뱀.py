from collections import deque
queue = deque()
timer = 0
startx = 3

def bang(yy, xx, now, dl):
    if now == 0:
        if dl == 'd':
            xx = xx+1
        elif dl == 'l':
            xx = xx-1
        else :
            yy = yy-1
    if now == 1:
        if dl == 'd':
            xx = xx-1
        elif dl == 'l':
            xx = xx+1
        else :
            yy = yy+1
    if now == 2:
        if dl == 'd':
            yy = yy-1
        elif dl == 'l':
            yy = yy+1
        else :
            xx = xx-1
    if now == 3:
        if dl == 'd':
            yy = yy+1
        elif dl == 'l':
            yy = yy-1
        else :
            xx = xx+1

    return yy, xx

n = int(input())
graph = [[0]*(n+2)]*(n+2)

k = int(input())
for _ in range(k):
    n, m = map(int, input().split())
    graph[n][m] = 1

now_y = 1
now_x = 1
l = int(input())
for _ in range(l):
    x, c = input().split()
    queue.append([x, c])

while queue:
    x, c = queue.popleft()
    if x+1 == timer:
        now_c = c
    else :
        timer = timer + 1
        now_c = 'f'
    ny, nx = bang(now_y, now_x, startx, c)
    if graph[ny][nx] == 1:
        graph[ny][nx] = -1
    elif graph[ny][nx] == 0:
        graph[ny][nx] = -1
    elif graph[ny][nx] == -1:
        result = timer

print(result)