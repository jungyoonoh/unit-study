# 10867번 중복 빼고 정렬하기 (Implementation) 
# https://www.acmicpc.net/problem/10867

N = int(input())
data = list(map(int, input().split()))
res = list(set(data))
res.sort()
print(*res)