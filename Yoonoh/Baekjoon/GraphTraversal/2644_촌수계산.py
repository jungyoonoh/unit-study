# 2644 촌수계산 (GraphTraversal) 
# https://www.acmicpc.net/problem/2644

N = int(input()) 
parent, child = map(int, input().split())

R = int(input())
info = [[] for _ in range(N+1)]

ans = -1
def search(idx, cnt, isVisited):
    global ans
    if idx == child:
        ans = cnt
        return

    for i in info[idx]:
        if not isVisited[i]:
            isVisited[i] = True
            search(i, cnt + 1, isVisited)
            isVisited[i] = False

for i in range(R):
    p, c = map(int, input().split())
    info[p].append(c)
    info[c].append(p)

isVisited = [False] * (N+1)
search(parent, 0, isVisited)
print(ans)