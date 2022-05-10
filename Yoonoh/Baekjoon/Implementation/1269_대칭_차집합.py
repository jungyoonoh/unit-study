# 1269번 스위치 켜고 끄기 (Implementation) 
# https://www.acmicpc.net/problem/1269

A, B = map(int, input().split())
d1 = set(list(map(int, input().split())))
d2 = set(list(map(int, input().split())))
d1 | d2 

common = d1 & d2

print(len(d1) + len(d2) - len(common) * 2) 