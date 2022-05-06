# 24049번 정원 (Implementation) 
# https://www.acmicpc.net/problem/24049

N, M = map(int, input().split()) # 세로와 가로

flower = [[-1 for _ in range(M+1)] for _ in range(N+1)]
col = list(map(int, input().split()))
row = list(map(int, input().split()))

for i in range(1, N+1):
    flower[i][0] = col[i-1]

for i in range(1, M+1):
    flower[0][i] = row[i-1]

for i in range(1, N+1):
    for j in range(1, M+1):
        flower[i][j] = 1 if flower[i-1][j] != flower[i][j-1] else 0
        
print(flower[N][M])