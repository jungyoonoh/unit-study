out = []

def DFS(depth, idx):
    if depth == 6:
        print(*out)
    elif depth > 6:
        return

    for i in range(idx, k):
        out.append(s[i])
        DFS(depth+1, i+1)
        out.pop()

while True:
    tc = list(map(int, input().split()))
    k = tc[0]
    s = tc[1:]

    if k == 0:
        exit(0)

    DFS(0, 0)
    print()