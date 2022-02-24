#20220224
#백준(투포인터) : 11728 배열 합치기 #https://www.acmicpc.net/problem/11728

n, m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
ab = a+b
ab.sort()
print(*ab)