#20220121
#백준(그리디) : 14247 나무자르기 
#https://www.acmicpc.net/problem/14247

n = int(input())
Hi = list(map(int,input().split()))
Ai = list(map(int,input().split()))
idx = []


for i in range(n):
  idx.append([i,Ai[i]])
idx.sort(key=lambda x:x[1])
tree = Hi[idx[0][0]]

for i in range(1,n):
  tree += Hi[idx[i][0]] + Ai[idx[i][0]]*(i) 

print(tree)


#아래로 풀면 답은 맞지만 시간초과
# n = int(input())
# Hi = list(map(int,input().split()))
# Ai = list(map(int,input().split()))
# idx = []
# tree = 0

# for i in range(n):
#   idx.append([i,Ai[i]])
# idx.sort(key=lambda x:x[1])

# for i in range(n):
#   tree += Hi[idx[i][0]]
#   Hi[idx[i][0]] = 0
#   for j in range(n):
#     Hi[j] = Hi[j] + Ai[j]

# print(tree)

