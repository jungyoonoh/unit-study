# 백준 11403 경로 찾기

import sys
input = sys.stdin.readline

# 노드가 500개 이하(100개)라서 플로이드 워셜 알고리즘 적용할 수 있는 문제
n = int(input())
graph = []

# 테이블 채우기
for i in range(n):
    graph.append(list(map(int, input().split())))

# 테이블 값이 0이면 경로가 없는 것이므로 무한대값 넣어줌
for i in range(n):
    for j in range(n):
        if not graph[i][j]:
            graph[i][j] = float('inf')

# 최단경로 업데이트
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 최단경로가 무한대값이면 경로가 없는 것이므로 0으로 바꿔주고, 무한대값이 아니라면 경로가 있는 것이므로 1로 바꿔줌
for i in range(n):
    for j in range(n):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0
        else:
            graph[i][j] = 1

# 정답 출력
for i in range(n):
    print(*graph[i], sep=' ')