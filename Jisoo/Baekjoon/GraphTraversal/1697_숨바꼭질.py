from collections import deque

n, k = map(int, input().split())
count = 0
queue = deque()

def BFS(start, goal):
    queue.append(start)

    while queue:
        x = queue.popleft()
        if x == goal:
            print(count)
        else:
            for ox in (start -1, start + 1, 2*start):
                if (0<=ox<100000):
                    count = count + 1
                    queue.append(ox)
        exit(0)

BFS(n, k)




