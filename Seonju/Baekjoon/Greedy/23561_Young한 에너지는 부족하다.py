# 백준 23561 Young한 에너지는 부족하다

import sys
input = sys.stdin.readline

n = int(input())
age = sorted(list(map(int, input().split())))

print(age[2*n-1] - age[n])