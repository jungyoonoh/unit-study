from collections import deque

a, b = map(int, input().split())
queue = deque()
queue.append([a, 1])

while True:
    #print(queue)

    a, cnt = queue.popleft()

    if (a == b):
        print(cnt)
        break

    dx1 = 2*a
    dx2 = 10*a + 1

    if (dx1<=b):
        queue.append([dx1, cnt+1])

    if (dx2<=b):
        queue.append([dx2, cnt+1])

    if not queue:
        print("-1")
        exit(0)

